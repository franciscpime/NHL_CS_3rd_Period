from numb3rs import validate

def test_string():
    assert validate("cat") == False


def test_more_255():
    assert validate("123.167.344.3") == False


def test_starts_with_0():
    assert validate("003.23.2.1") == False


def test_extra_number():
    assert validate("123.23.4.1.56") == False