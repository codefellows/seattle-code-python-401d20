import pytest

from dog_pack import Pack, Dog, Bullhuahua, Terrier, Puggle

def test_pack_oath():
    assert 'all for one, one for all' == Pack.get_pack_oath()

def test_lela_is_instance_of_correct_class():
    lela = Bullhuahua('Lela')
    assert isinstance(lela, Bullhuahua)


def test_lela_is_instance_of_parent_class(lela):
    assert isinstance(lela, Dog)


def test_lela_name():
    lela = Bullhuahua('Lela')
    assert lela.name == 'Lela'


def test_lela_breed():
    lela = Bullhuahua('Lela')
    assert lela.breed == 'bullhuahua'


def test_get_dogs():
    expected = [Bullhuahua('Lela'), Puggle('Chewy')]
    actual = Dog.get_dogs()
    assert actual == expected

def test_create_pack_from_data():
    data = """
    Rex,Terrier
    Jolene,Puggle
    Keanu,Bullhuahua
    """

    pack = Pack.create_from_data(data)

    assert pack.leader.name == 'Rex'


@pytest.fixture()
def lela():
    return Bullhuahua('Lela')

@pytest.fixture(autouse=True)
def clean():
    Dog.dog_list = []
