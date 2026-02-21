import twttr
from twttr import shorten

def test_vowels_lower():
    assert shorten("Francisco") == "Frncsc"


def test_numbers():
    assert shorten("1") == "1"


def test_space():
    assert shorten(" ") == " "


def test_vowels_upper():
    assert shorten("HOLA") == "HL"


def test_punctuation():
    assert shorten("Hi!") == "H!"
    