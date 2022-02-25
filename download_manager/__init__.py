from bs4 import BeautifulSoup
import requests
from typing import Tuple, Optional
from urllib import request
from models import Info
import time
from utils import get_extension
from tqdm import trange

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"}


def get_info(url: str) -> Info:
    if url[-1] == "/":
        url = url + "?nw=always"
    else:
        url = url + "/?nw=always"
    page = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(page.content, 'html.parser')
    first_page = bs.find("div", {"class": "gdtm"}).a['href']
    title = bs.title.text
    tds = list(map(lambda x: x.text, bs.find(id="gdd").table.find_all('td', {"class": "gdt2"})))
    pages = int(list(filter(lambda x: "pages" in x, tds))[0].replace("pages", "").strip())

    return Info(first_page=first_page, title=title, pages=pages)


def get_image_and_next(url: str) -> Tuple[str, Optional[str]]:
    page = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(page.content, 'html.parser')
    img_url = bs.find(id="i3").img['src']
    next_page = bs.find(id="next")['href']
    return img_url, next_page


def download_image(url: str, path: str, idx: int, ext: str):
    request.urlretrieve(url=url, filename=f"{path}/{idx}{ext}")


def download(info: Info, path: str):
    img_url, next_page = get_image_and_next(info.first_page)
    for idx in trange(info.pages, ascii=True, desc=info.title):
        tries = 0
        success = False
        while tries < 3 and not success:
            try:
                download_image(img_url, path, idx, get_extension(img_url))
                if idx != info.pages - 1:
                    img_url, next_page = get_image_and_next(next_page)
                success = True
            except Exception as e:
                print(f"[ERROR]: {e}")
                print(f"Try #{tries}")
                tries = tries + 1
                time.sleep(1 * tries)
