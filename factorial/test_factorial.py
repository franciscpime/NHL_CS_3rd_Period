import pytest
from factorial import factorize


def test_zero():
    assert factorize("0") == 1


def test_three():
    assert factorize("3") == 6


def test_negative():
    assert factorize("-1") == "Dumb!"


def test_len():
    assert factorize("9999") == "Too much"


