from typing import List
from PIL import Image


def generate_pdf(output_path: str, file_name: str, images: List[str]) -> str:
    filename = f"{output_path}\\{file_name}.pdf"
    print(f"Generating PDF for {filename}")
    imgs = [Image.open(img) for img in images]
    imgs[0].save(
        filename, "PDF", resolution=100.0, save_all=True, append_images=imgs[1:]
    )
    print(f"PDF {filename} generated")
    return filename
