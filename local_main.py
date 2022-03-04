from consolemenu import *
from consolemenu.items import *
from menu_selection import manga_download, zip_files, pdf, automate
from config import settings

base_path = settings.base_path


def main():
    menu = ConsoleMenu("Welcome to E-Hentai downloader", "Choose your selection")
    menu.append_item(FunctionItem("Download a comic", manga_download, [base_path]))
    menu.append_item(FunctionItem("Full Automate", automate, [base_path]))
    menu.show()
