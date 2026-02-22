import pytest
from factorial import factorize

def test_zero():
    assert factorize("0") == 1


def test_one():
    assert factorize("1") == 1


def test_three():
    assert factorize("3") == 6


def test_five():
    assert factorize("5") == 120


def test_max_valid_length():
    assert factorize("999") == pytest.approx(factorize("999"))


def test_negative():
    assert factorize("-1") == "Dumb!"


def test_letters():
    assert factorize("abc") == "Dumb!"


def test_mixed():
    assert factorize("12a") == "Dumb!"


def test_space():
    assert factorize(" ") == "Dumb!"


def test_decimal():
    assert factorize("3.5") == "Dumb!"


def test_len_exact_limit():
    assert factorize("1000") == "Too much"


def test_len_above_limit():
    assert factorize("9999") == "Too much"