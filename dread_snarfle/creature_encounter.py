from __future__ import annotations
from dataclasses import dataclass
from plug.abstract import Transform
from typing import Set

from dread_snarfle.model import CreatureModel, ItemModel, PlayerModel
from dread_snarfle.error import PlaceholderError


@dataclass
class CreatureEncounter(Transform):
    fqdn = 'dread_snarfle.transform.CreatureEncounter'
    creature: str
    player: str

    def required_authorizations(self) -> Set[str]:
        return {
            self.creature
        }

    @staticmethod
    def required_models() -> Set[str]:
        return {
            CreatureModel.fqdn,
            ItemModel.fqdn,
            PlayerModel.fqdn,
        }

    def required_keys(self) -> Set[str]:
        return {
            self.player,
            self.creature
        }

    @staticmethod
    def pack(registry, obj) -> dict:
        return {
            'player': obj.player,
            'creature': obj.creature,
        }

    @classmethod
    def unpack(cls, registry, payload) -> 'CreatureEncounter':
        return cls(
            player=payload['player'],
            creature=payload['creature'],
        )

    def verify(self, state_slice) -> None:
        creatures = state_slice[CreatureModel.fqdn]

        if self.intact <= 0:
            raise PlaceholderError('Already broken!')

        if creatures[self.creature].intact <= 0:
            raise PlaceholderError('Creature is dead!')

    def apply(self, state_slice) -> None:
        creatures = state_slice[CreatureModel.fqdn]
        creatures[self.creature].intact -= 50

        items = state_slice[ItemModel.fqdn]
        players = state_slice[PlayerModel.fqdn]
        item_hash = players[self.player].item
        items[item_hash].intact -= 50

        if creatures[self.creature].intact <= 0:
            if items[item_hash].names == None:
                items[item_hash].names == []

            items[item_hash].names.append('Slayer of ' + creatures[self.creature].name)
