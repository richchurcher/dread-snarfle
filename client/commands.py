from client.player import Player
from client.creature import Creature


def create_player():
    player = Player(None)
    print('Player key:', player.address, '\n')
    return player


def create_creature():
    creature = Creature(None)
    print('Creature key:', creature.address, '\n')
