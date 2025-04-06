import requests

from typing import Any, Dict, List, Union

# These models are based on the wallhaven API help docs here:
# https://wallhaven.cc/help/api

FILE_TYPE_MAP = {
    "image/jpeg": "jpg",
    "image/png": "png",
}


class WallhavenImage:
    def __init__(
        self,
        id: str,
        url: str,
        category: str,
        created_at: str,
        file_size: int,
        file_type: str,
        path: str,
        purity: str,
        ratio: str,
        resolution: str,
        short_url: str,
        source: str,
        **kwargs: Dict[Any, Any],
    ):
        self.id = id
        self.url = url
        self.category = category
        self.created_at = created_at
        self.file_size = file_size
        self.file_type = file_type
        self.path = path
        self.purity = purity
        self.ratio = ratio
        self.resolution = resolution
        self.short_url = short_url
        self.source = source
        self.data = b""
        if kwargs:
            self.__dict__.update(kwargs)


class WallhavenCollection:
    def __init__(
        self,
        id: int,
        label: str,
        public: int,
        views: int,
        count: int,
        contents: List = list(),
        **kwargs: Dict[Any, Any],
    ):
        self.id = id
        self.label = label
        self.public = bool(public)
        self.views = views
        self.count = count
        self.contents = contents
        if kwargs:
            self.__dict__.update(kwargs)

    def __eq__(self, other):
        # specifically excluding the views attribute
        # because the same collection could be viewed recently buty
        # not have any other changes. For the purpose of syncing,
        # we're only concerned with the contents of the collections
        return all(
            [
                self.id == other.id,
                self.label == other.label,
                self.public == other.public,
                self.count == other.count,
            ]
        )

    def __repr__(self):
        return (
            "Collection("
            f"id={self.id}, "
            f"label={self.label}, "
            f"public={int(self.public)}, "
            f"views={self.views}, "
            f"count={self.count}"
            ")"
        )

    def __str__(self):
        return repr(self)


class WallhavenTag:
    def __init__(
        self,
        id: int,
        name: str,
        alias: str,
        category_id: int,
        category: str,
        purity: str,
        created_at: str,
    ):
        self.id = id
        self.name = name
        self.alias = alias
        self.category_id = category_id
        self.category = category
        self.purity = purity
        self.created_at = created_at
