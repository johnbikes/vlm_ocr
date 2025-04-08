# code ref: https://github.com/johnbikes/vits-cifar10/blob/main/test_env.py

import os
from pathlib import Path

from dotenv import load_dotenv
from pdf2image import convert_from_path


def configur_env():
    load_dotenv()

    hf_hub_cache = os.getenv("HF_HUB_CACHE")
    hf_ds_cache = os.getenv("HF_DATASETS_CACHE")
    hf_home = os.getenv("HF_HOME")

    print(f"{hf_hub_cache = }. {hf_ds_cache = }, {hf_home = }")

    if hf_home is not None:
        os.environ['HF_HOME'] = hf_home
        print('Using HF_HOME')
    else:
        if hf_hub_cache is not None:
            os.environ['HF_HUB_CACHE'] = hf_hub_cache
            print('Using HF_HUB_CACHE')

        if hf_ds_cache is not None:
            os.environ['HF_DATASETS_CACHE'] = hf_ds_cache
            print('Using HF_DATASETS_CACHE')

def get_pdf_images(pdf_dir_path: Path = None, filter: str = None):
    print(f"grabbing pdf images using {filter = }")

    # grab from the env if not set
    if pdf_dir_path is None:
        pdf_dir = os.getenv("PDF_DIR")
        print(f"from env: {pdf_dir = }")
        assert pdf_dir is not None, f"{pdf_dir} must be set"
        pdf_dir_path = Path(pdf_dir)

    assert pdf_dir_path.is_dir(), f"{pdf_dir_path} must be a directory"

    images_dict = {}
    for path_i, pdf_path in enumerate(pdf_dir_path.glob('*.pdf')):
        if filter is not None and filter.lower() not in pdf_path.stem.lower():
            print(f"Skipping {pdf_path} because it does not match filter")
            continue

        print(f"Converting {pdf_path} to image")
    
        images = convert_from_path(str(pdf_path))
        
        # print('images', images)
        
        # for im_i, image in enumerate(images):
        #     image.save(f"{path_i}_{im_i}.png")

        images_dict[pdf_path.stem] = images

    return images_dict