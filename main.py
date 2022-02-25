from consolemenu import *
from consolemenu.items import *
from menu_selection import manga_download, zip_files

base_path = "F:\Furry"


def main():
    menu = ConsoleMenu("Welcome to E-Hentai downloader", "Choose your selection")
    menu.append_item(FunctionItem("Download a comic", manga_download, [base_path]))
    menu.append_item(FunctionItem("Zip Files", zip_files, [base_path]))
    menu.show()

if __name__ == '__main__':
    main()
