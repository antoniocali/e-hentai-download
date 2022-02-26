import shutil
from os import getcwd
from os.path import join


def generate_zip(base_path: str, filename: str) -> str:
    filepath = join(base_path, f"{filename}.zip")
    print(f"Zip File creation {filepath}")
    shutil.make_archive(filename, "zip", base_path, filename)
    shutil.move(f"{getcwd()}\\{filename}.zip", filepath)
    print(f"Zip File created for {filepath}")
    return filepath
