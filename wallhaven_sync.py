#!/usr/bin/env python3

import json
import logging
import os
import requests
import sys

from pprint import pprint
from types import SimpleNamespace

from wallhaven_lib.file_manager import FileManager
from wallhaven_lib.helpers import load_config_file
from wallhaven_lib.wallhaven_client import WallhavenClient
from wallhaven_lib.wallhaven_models import WallhavenCollection

CONFIG = SimpleNamespace(
    CONFIG_FILE="wallhaven_sync_conf.json",
    WALLHAVEN_API_BASE_URL="https://wallhaven.cc/api/v1/",
    LOGGING=SimpleNamespace(
        FILENAME="wallhaven_sync.log",
        FORMAT=(
            "%(asctime)s "
            "%(levelname)s "
            "%(module)s "
            "%(filename)s "
            "%(funcName)s "
            "%(message)s"
        ),
        LEVEL=logging.DEBUG,
    ),
)


def main(config):
    fm = FileManager(config.SYNC_BASE_PATH)
    wclient = WallhavenClient(
        base_url=config.WALLHAVEN_API_BASE_URL,
        username=config.USERNAME,
        api_key=config.API_KEY,
    )
    collections = wclient.get_collections()
    # some todos-
    # 1. for each collection, make sure a directory exists with that name
    # create two directories for images
    # - image metadata to store the json text for a given image
    # - image dir for the actual images themselves
    # create symlinks from the collection directory to the images in the image directory
    for collection in collections:
        fm.add_managed_collection_dir(collection.label)


if __name__ == "__main__":
    load_config_file(CONFIG, CONFIG.CONFIG_FILE)
    logging.basicConfig(
        filename=CONFIG.LOGGING.FILENAME,
        level=CONFIG.LOGGING.LEVEL,
        format=CONFIG.LOGGING.FORMAT,
    )
    logging.info("Starting wallhaven_sync.py")
    logging.debug(f"Calling main with config {CONFIG=}")
    main(config=CONFIG)
    logging.info("Complete, exiting")
    sys.exit(0)
