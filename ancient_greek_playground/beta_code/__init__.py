import unicodedata

beta_code_to_unicode_mapping = {
    # DIACRITICS
    ")": "\u0313",
    "(": "\u0314",
    "/": "\u0301",
    "=": "\u0302",
    "\\": "\u0300",
    "+": "\u0308",
    "|": "\u0345",
    "&": "\u0304",
    "'": "\u0306",
    ":": "\u0308",
    # UPPERCASE
    "A": "Α",
    "B": "Β",
    "G": "Γ",
    "D": "Δ",
    "E": "Ε",
    "V": "Ϝ",
    "Z": "Ζ",
    "H": "Η",
    "Q": "Θ",
    "I": "Ι",
    "K": "Κ",
    "L": "Λ",
    "M": "Μ",
    "N": "Ν",
    "C": "Ξ",
    "O": "Ο",
    "P": "Π",
    "R": "Ρ",
    "S": "Σ",
    "S1": "Σ",
    "S2": "Σ",
    "S3": "Ϲ",
    "J": "Σ",
    "T": "Τ",
    "U": "Υ",
    "F": "Φ",
    "X": "Χ",
    "Y": "Ψ",
    "W": "Ω",
    # LOWERCASE
    "a": "α",
    "b": "β",
    "g": "γ",
    "d": "δ",
    "e": "ε",
    "v": "ϝ",
    "z": "ζ",
    "h": "η",
    "q": "θ",
    "i": "ι",
    "k": "κ",
    "l": "λ",
    "m": "μ",
    "n": "ν",
    "c": "ξ",
    "o": "ο",
    "p": "π",
    "r": "ρ",
    "s": "σ",
    "s1": "σ",
    "s2": "ς",
    "s3": "ϲ",
    "j": "ς",
    "t": "τ",
    "u": "υ",
    "f": "φ",
    "x": "χ",
    "y": "ψ",
    "w": "ω",
}


# TODO: just for fun
# compare with: https://github.com/perseids-tools/beta-code-py
def beta_code_to_unicode(s: str):
    s_len = len(s)
    converted = ""

    i = 0
    while i < s_len:
        l = s[i]

        # sloppy sigma handling :P
        if l == "s" or l == "S":
            if i < s_len - 1:
                if s[i + 1] in {"1", "2", "3"}:
                    l += s[i + 1]
                    i += 1
                elif s[i + 1] not in beta_code_to_unicode_mapping:
                    l += "2"
            else:
                l += "2"

        if l in beta_code_to_unicode_mapping:
            converted += beta_code_to_unicode_mapping[l]
        else:
            converted += l

        i += 1

    return unicodedata.normalize("NFC", converted)
