import pytest

from ancient_greek_playground import beta_code_to_unicode
from ancient_greek_playground.normalization import replace_grave_with_acutus


@pytest.mark.parametrize(
    ["input_word", "expected"],
    [
        (
            beta_code_to_unicode("tata\\"),
            beta_code_to_unicode("tata/"),
        ),
    ],
)
def test_replace_grave_with_acutus(input_word: str, expected: str):
    assert replace_grave_with_acutus(input_word) == expected
