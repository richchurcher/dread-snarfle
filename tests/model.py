import pytest

from dread_snarfle.model import ItemModel


@pytest.fixture
def creature():
    from dread_snarfle.model import CreatureModel
    return CreatureModel(100, 'Confused Wumpus')


def test_creature_constructor(creature):
    assert creature.intact == 100
    assert creature.name == 'Confused Wumpus'


def test_item_constructor():
    names = [
        'Slayer of Wumpuses',
        'Scourge of the Wombat'
    ]
    repairs = [
        {'description': 'Clean and polish', 'skill': 5},
        {'description': 'Replace handle', 'skill': 3},
    ]
    qualities = {
        'cfsfatwpt': 33,
        'vsWombat': 1,
        'vsWumpus': 2
    }
    model = ItemModel(
        100,
        'Tarnished Kitchen Knife',
        names,
        repairs,
        qualities
    )

    assert model.intact == 100
    assert model.name == 'Tarnished Kitchen Knife'
    assert model.names == names
    assert model.repairs == repairs
    assert model.qualities == qualities
