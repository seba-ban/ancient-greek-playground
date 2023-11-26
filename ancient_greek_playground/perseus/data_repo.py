from dataclasses import dataclass, field
from pathlib import Path

from .constants import CANONICAL_GREEK_LIT_DATA
from .models import Author, AuthorNameT, WorkNameT
from .xml import (
    METADATA_FILENAME,
    extract_author_metadata,
    extract_work_metadata,
    get_greek_text,
)


def traverse_data_folder(p: Path = CANONICAL_GREEK_LIT_DATA):
    authors: dict[str, Author] = {}
    for author_folder in p.iterdir():
        if not author_folder.is_dir():
            continue

        if not (author_folder / METADATA_FILENAME).exists():
            print(f"Author {author_folder} does not have metadata file")
            continue

        author = extract_author_metadata(str(author_folder / METADATA_FILENAME))
        if author.name in authors:
            print(f"Author {author.name} already exists")

        authors[author.name.lower()] = author

        for work_folder in author_folder.iterdir():
            if not work_folder.is_dir():
                continue

            if not (work_folder / METADATA_FILENAME).exists():
                print(f"Work {work_folder} does not have metadata file")
                continue

            work = extract_work_metadata(str(work_folder / METADATA_FILENAME))
            author.works[work.name.lower()] = work

    return authors


@dataclass
class DataRepo:
    perseus_data_folder: Path = CANONICAL_GREEK_LIT_DATA
    authors: dict[str, Author] = field(default_factory=traverse_data_folder)

    def author_names(self):
        return sorted(self.authors.keys())

    def works_by_author(
        self, *author_names: AuthorNameT
    ) -> dict[AuthorNameT, list[WorkNameT]]:
        if not author_names:
            names = set(self.authors.keys())
        else:
            names = set(author_names)

        return {
            author_name: sorted(author.works.keys())
            for author_name, author in self.authors.items()
            if author_name in names
        }

    def read_work(self, author_name: AuthorNameT, work_name: WorkNameT):
        author = self.authors[author_name]
        work = author.works[work_name]

        for file in (
            self.perseus_data_folder / work.parent_folder() / work.folder()
        ).iterdir():
            if file.suffix.lower() == ".xml":
                text = get_greek_text(str(file))
                if text:
                    return text
        return ""

    def read_author_works(self, author_name: AuthorNameT) -> dict[WorkNameT, str]:
        return {
            work_name: self.read_work(author_name, work_name)
            for work_name in self.authors[author_name].works.keys()
        }
