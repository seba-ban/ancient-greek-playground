from typing import NamedTuple

from .constants import CANONICAL_GREEK_LIT_DATA

AuthorNameT = str
WorkNameT = str


class Work(NamedTuple):
    name: str
    urn: str

    def folder(self):
        return self.urn.split(".")[1]

    def parent_folder(self):
        return self.urn.split(".")[0].split(":")[3]

    def path(self):
        return CANONICAL_GREEK_LIT_DATA / self.parent_folder() / self.folder()


class Author(NamedTuple):
    name: str
    urn: str
    works: dict[str, Work]

    def folder(self):
        return self.urn.split(":")[3]
