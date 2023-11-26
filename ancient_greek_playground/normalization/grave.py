import unicodedata

GRAVE = "\u0300"
ACUTUS = "\u0301"


def replace_grave_with_acutus(word: str):
    if not unicodedata.is_normalized("NFC", word):
        raise ValueError("expected word to be normalized")

    for i, letter in enumerate(reversed(word)):
        decomposed = unicodedata.decomposition(letter).split(" ")
        try:
            dec_idx = decomposed.index("0300")
            decomposed[dec_idx] = "0301"
            normalized = unicodedata.normalize(
                "NFC", "".join(map(lambda s: chr(int(s, 16)), decomposed))
            )
            return (
                word[: (curr_idx := len(word) - i - 1)]
                + normalized
                + word[curr_idx + 1 :]
            )
        except ValueError:
            continue

    return word
