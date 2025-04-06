#!/usr/bin/env python3

import json
import logging
import os
import requests
import sys

from pprint import pprint
from types import SimpleNamespace

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
        LEVEL=logging.DEBUG
    )
)


def experimental_main(config):
    # get collections = https://wallhaven.cc/api/v1/collections?apikey=<API KEY>
    base_url = config.WALLHAVEN_API_BASE_URL
    collections_url = base_url + "collections"
    params = {"apikey": config.API_KEY}
    collections = requests.get(collections_url, params=params)
    print(collections)
    collection_data = json.loads(collections.text)["data"]
    pprint(collection_data)
    collection_list = [WallhavenCollection(**col) for col in collection_data]
    collection_list.sort(key=lambda collection: collection.label.lower())
    pprint(collection_list)

    tmp_col = collection_list[5].id
    tmp = requests.get(collections_url + "/AntsyDC/" + str(tmp_col), params=params)
    pprint(json.loads(tmp.text))


def main(config):
    os.makedirs(config.SYNC_BASE_PATH, exist_ok=True)
    wclient = WallhavenClient(
        base_url=config.WALLHAVEN_API_BASE_URL,
        username=config.USERNAME,
        api_key=config.API_KEY,
    )
    collections = wclient.get_collections()


if __name__ == "__main__":
    load_config_file(CONFIG, CONFIG.CONFIG_FILE)
    # experimental_main(config=CONFIG)
    logging.basicConfig(
        filename=CONFIG.LOGGING.FILENAME,
        level=CONFIG.LOGGING.LEVEL,
        format=CONFIG.LOGGING.FORMAT
    )
    logging.info("Starting wallhaven_sync.py")
    logging.debug(f"Calling main with config {CONFIG=}")
    main(config=CONFIG)
    logging.info("Complete, exiting")
    sys.exit(0)
