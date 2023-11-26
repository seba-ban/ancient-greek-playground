import pytest

from ancient_greek_playground.beta_code import beta_code_to_unicode


# TODO: use this: https://github.com/perseids-tools/beta-code-py/blob/master/tests/test_beta_code.py
@pytest.mark.parametrize(
    ["beta_code", "expected"],
    [
        ("a)= deile/, a)= deilw/, a)= deiloi/,", "ἀ̂ δειλέ, ἀ̂ δειλώ, ἀ̂ δειλοί,"),
        ("a)= ma/kar", "ἀ̂ μάκαρ"),
        ("a)blabei=s", "ἀβλαβει̂ς"),
        ("a)a/baktoi:", "ἀάβακτοϊ"),
        ("a)/oros", "ἄορος"),
        ("a)/oros2", "ἄορος"),
        ("a)/oros3", "ἄοροϲ"),
    ],
)
def test_beta_code_to_unicode(beta_code: str, expected: str):
    assert beta_code_to_unicode(beta_code) == expected
