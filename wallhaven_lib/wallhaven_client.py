# Client is based on the wallhaven API help docs here:
# https://wallhaven.cc/help/api

import logging
import requests

from typing import Union

from .wallhaven_models import WallhavenCollection


class WallhavenClient:
    def __init__(self, base_url: str, username: str, api_key: str):
        logging.debug("Initializing Wallhaven API Client")
        self.base_url = base_url
        self.username = username
        self.api_key = api_key
        self.base_get_params = {"apikey": api_key}
        self.url_templates = {
            "image": base_url + "w/{image_id}",
        }
        logging.debug(f"URL templates initialized: {self.url_templates=}")
        self.urls = {"collections": base_url + "collections"}
        logging.debug(f"static URLs initialized: {self.urls=}")
        logging.debug("Client initialization complete")

    def get_collections(self, user: Union[str, None] = None):
        logging.info(f"Gathering user collections for {self.username}")
        result = requests.get(self.urls.get("collections"), params=self.base_get_params)
        collections_json_result = result.json()
        logging.debug(f"{collections_json_result=}")
        collection_list = [
            WallhavenCollection(**collection)
            for collection in collections_json_result["data"]
        ]
        logging.debug(f"Retrived collections: {collection_list=}")
        return collection_list

    def get_image_metadata(self, image_id):
        pass

    def download_image_by_id(self, image_id):
        pass

    def download_image_by_url(self, url):
        logging.info(f"Downloading image {url=}")
        result = requests.get(url, params={"apikey": self.api_key})
        print(dir(result))
        return result.content
