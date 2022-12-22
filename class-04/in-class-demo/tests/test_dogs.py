import pytest
from dog_pack.dogs import Dog, Boxer, DogPack, Puggle


def test_dog_exists():
    assert Dog


def test_dog_name():
    kalua = Dog("Kalua")
    actual = kalua.name
    expected = "Kalua"
    assert actual == expected


def test_boxer_name():
    brock = Boxer("Brock")
    actual = brock.name
    expected = "Brock"
    assert actual == expected


def test_boxer_jump():
    brock = Boxer("Brock", 21)
    actual = brock.jump
    expected = 21
    assert actual == expected


def test_boxer_no_name():
    pooch = Boxer()
    actual = pooch.name
    expected = "unknown"
    assert actual == expected


def test_boxer_name2():
    marv = Boxer("Marv")
    actual = marv.name
    expected = "Marv"
    assert actual == expected


def test_boxer_str():
    marv = Boxer("Marv")
    # actual = marv.__str__()
    actual = str(marv) # same as line above
    expected = "Marv"
    assert actual == expected


# def test_boxer_greet():
#     marv = Boxer("Marv")
#     actual = marv.greet()
#     expected = "The name's Marv. Pleasure."
#     assert actual == expected


def test_boxer_greet(marv):
    # marv = Boxer("Marv")
    actual = marv.greet()
    expected = "The name's Marv. Pleasure."
    assert actual == expected


def test_empty_dogpack():
    pack = DogPack()
    actual = pack.dogs
    expected = []
    assert actual == expected


def test_two_in_dogpack():
    dogs = [Boxer("Marv"), Puggle("Lela")]
    pack = DogPack(dogs)
    actual = len(pack.dogs)
    expected = 2
    assert actual == expected


def test_dogpack_str():
    dogs = [Boxer("Marv"), Puggle("Lela")]
    pack = DogPack(dogs)
    actual = str(pack)
    expected = "Marv Lela"
    assert actual == expected


def test_dogpack_repr():
    dogs = [Boxer("Marv"), Puggle("Lela")]
    pack = DogPack(dogs)
    actual = pack.__repr__()
    expected = "DogPack([Boxer('Marv'), Puggle('Lela')])"
    assert actual == expected


# ### FIXTURES! ###

@pytest.fixture
def marv():
    return Boxer("Marv")

