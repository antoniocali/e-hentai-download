from os.path import join


def get_extension(url: str) -> str:
    last_dot = url.rfind(".")
    return url[last_dot:]


def sanitize_path(base_path: str, name: str) -> str:
    return join(base_path, name.replace("|", "").replace(":", ""))
