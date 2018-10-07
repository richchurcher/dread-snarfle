import pytest


@pytest.fixture
def creature():
    from dread_snarfle.model import CreatureModel
    return CreatureModel(100, 'Confused Wumpus')


@pytest.fixture
def item_properties():
    return {
        'names': [
            'Slayer of Wumpuses',
            'Scourge of the Wombat'
        ],
        'repairs': [
            {'description': 'Clean and polish', 'skill': 5},
            {'description': 'Replace handle', 'skill': 3},
        ],
        'qualities': {
            'cfsfatwpt': 33,
            'vsWombat': 1,
            'vsWumpus': 2
        }
    }


@pytest.fixture
def item(item_properties):
    from dread_snarfle.model import ItemModel
    return ItemModel(
        100,
        'Tarnished Kitchen Knife',
        item_properties['names'],
        item_properties['repairs'],
        item_properties['qualities']
    )


@pytest.fixture
def player():
    from dread_snarfle.model import PlayerModel
    return PlayerModel(100, 'Testy McTesterson', '1234567ABCDE')


def test_creature_constructor(creature):
    assert creature.intact == 100
    assert creature.name == 'Confused Wumpus'


def test_item_constructor(item, item_properties):
    assert item.intact == 100
    assert item.name == 'Tarnished Kitchen Knife'
    assert item.names == item_properties['names']
    assert item.repairs == item_properties['repairs']
    assert item.qualities == item_properties['qualities']


def test_player_constructor(player):
    assert player.intact == 100
    assert player.name == 'Testy McTesterson'
    assert player.model == '1234567ABCDE'
