from os.path import exists, join, isdir, isfile
from os import makedirs, listdir
from download_manager import get_info, download
from drive_manager import upload_file
from models import Info
from pdf_creation import generate_pdf
from telegram_manager import send_pic
from utils import sanitize_path

from zip_manager import generate_zip

folder_id = "1X5tM-OfwcS6en5qbQV_XeJWnQIGp767z"


def manga_download(base_path: str) -> Info:
    input_url = input("insert url\n")
    info = get_info(input_url)
    print(info)
    path = sanitize_path(base_path=base_path, name=info.title)
    if not exists(path):
        print(f"Creating folder: {path}")
        makedirs(path)

    download(info, path)
    print(f"Manga {info.title} downloaded")
    return info


def zip_files(base_path: str):
    folders = [elem for elem in listdir(base_path) if isdir(join(base_path, elem))]
    for elem in folders:
        generate_zip(base_path=base_path, filename=elem)


def pdf(base_path: str):
    folders = [elem for elem in listdir(base_path) if isdir(join(base_path, elem))]
    for folder in folders:
        images = [join(base_path, folder, elem) for elem in listdir(join(base_path, folder)) if
                  isfile(join(base_path, folder, elem))]
        generate_pdf(base_path, folder, images)


def automate(base_path: str):
    info = manga_download(base_path=base_path)
    filename = info.title
    images = [join(base_path, filename, elem) for elem in listdir(join(base_path, filename)) if
              isfile(join(base_path, filename, elem))]
    if info.pages > 70:
        path_file = generate_zip(base_path=base_path, filename=filename)
    else:
        path_file = generate_pdf(base_path, filename, images)
    uploaded = upload_file(filename=filename, local_file=path_file, folder_id=folder_id)
    if uploaded:
        send_pic(photo_path=images[0], text=filename)
