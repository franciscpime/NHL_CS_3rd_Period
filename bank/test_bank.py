import bank
from bank import value

def test_specific():
    assert value("hello") == "$0"


def test_start_h():
    assert value("holla") == "$20"


def test_others():
    assert value("Salut") == "$100"
