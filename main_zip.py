from os import path
from os import listdir, getcwd
import shutil

base_path = "F:\Furry"


def main():
    folders = [elem for elem in listdir(base_path) if path.isdir(path.join(base_path, elem))]
    print(folders)
    for elem in folders:
        print(elem)
        shutil.make_archive(elem, "zip", base_path, elem)
        shutil.move(f"{getcwd()}\\{elem}.zip", path.join(base_path, f"{elem}.zip"))



if __name__ == "__main__":
    main()
