from os.path import join
import shutil
import re

E_HENTAI_REGEX = re.compile('https://e-hentai\.org/g/\d{7}/[a-zA-Z0-9]{10}(/|$)')


def get_extension(url: str) -> str:
    last_dot = url.rfind(".")
    return url[last_dot:]


def sanitize_name(name: str) -> str:
    return name.replace("|", "").replace(":", "")


def sanitize_path(base_path: str, name: str) -> str:
    return join(base_path, sanitize_name(name))


def check_ehentai(url: str) -> bool:
    return True if E_HENTAI_REGEX.match(url) else False


def delete_folder(path: str) -> bool:
    try:
        shutil.rmtree(path)
        return True
    except:
        return False
