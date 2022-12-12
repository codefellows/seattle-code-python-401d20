from roman import to_arabic
def test_1000():
    actual = to_arabic('M')
    expected = 1000
    assert actual == expected

def test_900():
    actual = to_arabic('cm')
    expected = 900
    assert actual == expected

def test_1984():
    actual = to_arabic('mcmlxxxiv')
    expected = 1984
    assert actual == expected

def test_3999():
    actual = to_arabic('mmmcmxcix')
    expected = 3999
    assert actual == expected
