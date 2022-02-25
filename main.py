from bs4 import BeautifulSoup
import requests
from typing import Tuple, Optional
from urllib import request
from dataclasses import dataclass
from os.path import join, exists
from os import makedirs
import time

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"}
base_path = "F:\Furry"


@dataclass
class Info:
    first_page: str
    title: str


def get_info(url: str) -> Info:
    page = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(page.content, 'html.parser')
    first_page = bs.find("div", {"class": "gdtm"}).a['href']
    title = bs.title.text

    return Info(first_page=first_page, title=title)


def get_image_and_next(url: str) -> Tuple[str, Optional[str]]:
    page = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(page.content, 'html.parser')
    img_url = bs.find(id="i3").img['src']
    next_page = bs.find(id="next")['href']
    if next_page == url:
        next_page = None
    return img_url, next_page


def get_extension(url: str) -> str:
    last_dot = url.rfind(".")
    return url[last_dot:]


def download_image(url: str, path: str, idx: int, ext: str):
    request.urlretrieve(url=url, filename=f"{path}/{idx}{ext}")


def sanitize_path(name: str) -> str:
    return join(base_path, name.replace("|", ""))


def main():
    input_url = input("insert url\n")
    idx = 0
    info = get_info(input_url)
    print(info)
    path = sanitize_path(info.title)
    if not exists(path):
        print(f"Creating folder: {path}")
        makedirs(path)
    img_url, next_page = get_image_and_next(info.first_page)
    download_image(img_url, path, idx, get_extension(img_url))
    print(f"Downloaded page {idx}")
    time.sleep(0.5)
    while next_page:
        idx = idx + 1
        img_url, next_page = get_image_and_next(next_page)
        download_image(img_url, path, idx, get_extension(img_url))
        print(f"Downloaded page {idx}")
        time.sleep(1)
    print("done")


if __name__ == '__main__':
    main()
