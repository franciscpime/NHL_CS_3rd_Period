import plates
from plates import is_valid


def test_size():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_letters():
    assert is_valid("A1") == False
    assert is_valid("1A") == False


def test_isalnum():
    assert is_valid(" ") == False
    assert is_valid("AA@12") == False


def test_zero():
    assert is_valid("AA0") == False


def test_number_placement():
    assert is_valid("AA1A") == False
    assert is_valid("AB12C") == False


def test_valid_cases():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("AB123") == True