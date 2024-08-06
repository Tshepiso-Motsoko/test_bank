from bank import value


def test_value():
    # Test with greeting starting with "hello"
    assert value("Hello, World!") == 0

    # Test with greeting starting with "h" (but not "hello")
    assert value("Hey there!") == 20

    # Test with greeting starting with other letters
    assert value("What's up?") == 100

    # Test with greeting starting with uppercase "H"
    assert value("How are you?") == 20

    # Test with greeting starting with uppercase "HELLO"
    assert value("HELLO, world!") == 0

    # Test with greeting starting with "h" and other characters
    assert value("haha!") == 20

    # Test with empty greeting
    assert value("") == 100


if __name__ == "__main__":
    test_value()
