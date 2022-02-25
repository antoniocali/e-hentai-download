from os.path import exists, join, isdir
from os import makedirs, listdir, getcwd
from download_manager import get_info, download, get_image_and_next
from utils import sanitize_path
import shutil


def manga_download(base_path: str):
    input_url = input("insert url\n")
    info = get_info(input_url)
    print(info)
    path = sanitize_path(base_path=base_path, name=info.title)
    if not exists(path):
        print(f"Creating folder: {path}")
        makedirs(path)

    download(info, path)
    print("done")


def zip_files(base_path: str):
    folders = [elem for elem in listdir(base_path) if isdir(join(base_path, elem))]
    print(folders)
    for elem in folders:
        print(elem)
        shutil.make_archive(elem, "zip", base_path, elem)
        shutil.move(f"{getcwd()}\\{elem}.zip", join(base_path, f"{elem}.zip"))
