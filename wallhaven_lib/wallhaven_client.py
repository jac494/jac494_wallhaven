# Client is based on the wallhaven API help docs here:
# https://wallhaven.cc/help/api

import requests

from typing import Union


class WallhavenClient:
    def __init__(self, base_url: str, username: str, api_key: str):
        self.base_url = base_url
        self.username = username
        self.api_key = api_key
        self.url_templates = {
            "image": base_url + "w/{image_id}",
        }
        self.urls = {"collections": base_url + "collections"}

    def get_collections(self, user: Union[str, None] = None):
        pass

    def get_image_metadata(self, image_id):
        pass

    def download_image_by_id(self, image_id):
        pass

    def download_image_by_url(self, url):
        result = requests.get(url, params={"apikey": self.api_key})
        return result.text
