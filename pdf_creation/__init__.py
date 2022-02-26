from typing import List
from PIL import Image


def generate_pdf(output_path: str, file_name: str, images: List[str]):
    imgs = [Image.open(img) for img in images]
    imgs[0].save(
        f"{output_path}\\{file_name}.pdf", "PDF", resolution=100.0, save_all=True, append_images=imgs[1:]
    )

