# code ref: https://github.com/johnbikes/vits-cifar10/blob/main/test_env.py

import os

from dotenv import load_dotenv


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