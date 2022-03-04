from telegram import Bot
from drive_manager import upload_file
from models import Info
from os.path import exists, join, isfile
from os import makedirs, listdir, remove
from pdf_creation import generate_pdf
from zip_manager import generate_zip
from config import settings
from typing import Optional
from utils import delete_folder, sanitize_path
from download_manager import download

folder_id = settings.folder_id


def send_pic(photo_path: str, text: str, bot: Optional[Bot] = None) -> bool:
    if not bot:
        bot = Bot(token=settings.telegram_token)
    bot.send_photo(photo=open(photo_path, 'rb'), caption=f"Appena aggiunto {text}!",
                   chat_id=settings.telegram_channel_id)


def telegram_download(bot: Bot, base_path: str, info: Info) -> bool:
    downloaded = telegram_manga_download(base_path=base_path, info=info)
    if downloaded:
        filename = info.title
        images = sorted([join(base_path, filename, elem) for elem in listdir(join(base_path, filename)) if
                         isfile(join(base_path, filename, elem))])
        if info.pages > 70:
            path_file = generate_zip(base_path=base_path, filename=filename)
        else:
            path_file = generate_pdf(base_path, filename, images)
        uploaded = upload_file(filename=filename, local_file=path_file, folder_id=folder_id)
        if uploaded:
            send_pic(photo_path=images[0], text=filename, bot=bot)
            remove(path_file)
            delete_folder(join(base_path, filename))


def telegram_manga_download(base_path: str, info: Info) -> bool:
    try:
        print(info)
        path = sanitize_path(base_path=base_path, name=info.title)
        if not exists(path):
            print(f"Creating folder: {path}")
            makedirs(path)
        download(info, path)
        print(f"Manga {info.title} downloaded")
        return True
    except:
        return False
