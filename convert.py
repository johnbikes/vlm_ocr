import os
from pathlib import Path

from dotenv import load_dotenv
from pdf2image import convert_from_path


def main():
    load_dotenv()

    pdf_dir = os.getenv("PDF_DIR")
    
    print(f"{pdf_dir = }")

    assert pdf_dir is not None, f"{pdf_dir} must be set"
    pdf_dir_path: Path = Path(pdf_dir)
    assert pdf_dir_path.is_dir(), f"{pdf_dir_path} must be a directory"

    for path_i, pdf_path in enumerate(pdf_dir_path.glob('*.pdf')):
        print(f"Converting {pdf_path} to image")
    
        images = convert_from_path(str(pdf_path))

        print('images', images)

        for im_i, image in enumerate(images):
            image.save(f"{path_i}_{im_i}.png")

if __name__ == '__main__':
    main()