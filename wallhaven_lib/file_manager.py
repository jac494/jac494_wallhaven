import logging
import os

from typing import List, Union

class FileManager:
    def __init__(self, base_path: str, collection_dir: str = 'collections', collection_list: Union[None, List[str]] = None):
        self.base_path = base_path
        FileManager._ensure_dir(base_path)
        self.image_dir = os.path.join(base_path, 'images')
        FileManager._ensure_dir(self.image_dir)
        self.image_metadata_dir = os.path.join(self.image_dir, 'image_metadata')
        FileManager._ensure_dir(self.image_metadata_dir)
        self.collection_path = os.path.join(base_path, collection_dir)
        FileManager._ensure_dir(self.collection_path)
        self.collection_directory_map = dict()
        if collection_list is not None:
            for collection_label in collection_list:
                self.add_managed_collection_dir(collection_label)

    @classmethod
    def _ensure_dir(cls, path):
        # really just setting exist_ok on makedirs calls
        os.makedirs(path, exist_ok=True)
    
    def add_managed_collection_dir(self, collection_label):
        logging.debug(f"Adding {collection_label=} to managed collection directories")
        self.collection_directory_map[collection_label] = os.path.join(
            self.collection_path, collection_label
        )
        FileManager._ensure_dir(self.collection_directory_map[collection_label])

