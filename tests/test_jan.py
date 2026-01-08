import pytest
from src.jan import vowel_case


def test_vowel_case():
    assert vowel_case("Hello World") == "hEllO wOrld"
