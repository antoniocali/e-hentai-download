from setuptools import setup

setup(
    name='e-hentai-download',
    packages=['utils', 'models', 'resources', 'zip_manager', 'pdf_creation', 'drive_manager', 'menu_selection',
              'download_manager', 'telegram_manager'],
    author='Tizianoreica',
    description='Downloader for e-hentai',
    install_requires=["setuptools",
                      "dynaconf",
                      "Pillow",
                      "PyDrive",
                      "requests",
                      "beautifulsoup4",
                      "tqdm",
                      "python-telegram-bot"]
)
