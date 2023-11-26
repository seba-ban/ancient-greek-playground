from pathlib import Path

TMP_DIR = Path(__file__).parent.parent.parent / ".tmp"

TMP_DIR_PROCESSED = TMP_DIR / "processed"
TMP_DIR_PROCESSED.mkdir(parents=True, exist_ok=True)

TMP_DIR_REPOS = TMP_DIR / "repos"
TMP_DIR_REPOS.mkdir(parents=True, exist_ok=True)
