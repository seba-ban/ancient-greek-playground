from git import Repo

from .constants import (
    CANONICAL_GREEK_LIT,
    CANONICAL_GREEK_LIT_DATA,
    CANONICAL_GREEK_LIT_ROOT,
)


def download_canonical_greek_lit():
    if CANONICAL_GREEK_LIT_DATA.exists():
        print(f"canonical-greekLit already downloaded to {CANONICAL_GREEK_LIT_ROOT}")
        return
    Repo.clone_from(CANONICAL_GREEK_LIT, CANONICAL_GREEK_LIT_ROOT)
    print(f"Downloaded canonical-greekLit to {CANONICAL_GREEK_LIT_ROOT}")
