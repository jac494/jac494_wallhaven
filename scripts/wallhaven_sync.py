#!/usr/bin/env python3

import json
import os
import requests

from pprint import pprint
from types import SimpleNamespace

from wallhaven_lib.helpers import load_config_file
from wallhaven_lib.wallhaven_client import WallhavenClient
from wallhaven_lib.wallhaven_models import WallhavenCollection

CONFIG = SimpleNamespace(
    CONFIG_FILE="wallhaven_sync_conf.json",
    WALLHAVEN_API_BASE_URL="https://wallhaven.cc/api/v1/",
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
    os.makedirs(config.SYNC_BASE_PATH, exists_ok=True)
    wclient = WallhavenClient(
        base_url=config.WALLHAVEN_API_BASE_URL,
        username=config.USERNAME,
        api_key=config.API_KEY,
    )
    img_data = wclient.download_image_by_url(
        "https://w.wallhaven.cc/full/gp/wallhaven-gproj3.png"
    )
    with open(os.path.join(config.SYNC_BASE_PATH, "wallhaven-gproj3.png"), "wb") as fp:
        fp.write(img_data)


if __name__ == "__main__":
    load_config_file(CONFIG, CONFIG.CONFIG_FILE)
    # experimental_main(config=CONFIG)
    main(config=CONFIG)
