import bank
from bank import value

def test_specific():
    assert value("hello") == 0


def test_start_h():
    assert value("holla") == 20


def test_others():
    assert value("Salut") == 100


def test_complete_sentence():
    assert value("Hello my friend") == 0