import pytest
from fuel import convert, gauge

def test_normal():
    assert convert("1/2") == 50
    assert gauge(50) == "50%"


def test_value_error():
    with pytest.raises(ValueError):
        convert("3/2")

    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("5/-1")
    
    with pytest.raises(ValueError):
        convert("-5/1")

    with pytest.raises(ValueError):
        convert("1.5/2")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    
def test_special():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
