import os
from pathlib import Path

from dotenv import load_dotenv
from pdf2image import convert_from_path

from utils import get_pdf_images


def main():
    load_dotenv()

    # will use the env if pdf_dir_path not passed in
    pdf_images_dict = get_pdf_images(filter=os.getenv("PDF_DIR_FILTER"))

    for path_name, pdf_images in pdf_images_dict.items():

        for im_i, image in enumerate(pdf_images):
            image.save(f"{path_name}_{im_i}.png")

if __name__ == '__main__':
    main()