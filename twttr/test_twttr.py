import twttr
from twttr import shorten

def test_vowels():
    assert shorten("Francisco") == "Frncsc"


def test_numbers():
    assert shorten("1") == "Just Letters!"


def test_space():
    assert shorten(" ") == "Write Something!"