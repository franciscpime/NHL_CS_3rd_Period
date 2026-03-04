from um import count

def test_single_um():
    assert count("um") == 1


def test_multiple_um():
    assert count("um, um, um") == 3


def test_case_insensitive():
    assert count("Um, thanks for the album.") == 1


def test_not_inside_words():
    assert count("album yummy umbrella") == 0


def test_mixed():
    assert count("Um, thanks, um...") == 2
