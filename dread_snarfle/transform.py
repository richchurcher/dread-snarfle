from __future__ import annotations
from dataclasses import dataclass
from plug.abstract import Transform
from typing import Set

from dread_snarfle.model import CreatureModel, ItemModel
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
        #  item = state_slice[ItemModel.fqdn]

        if self.intact <= 0:
            raise PlaceholderError('Already broken!')

    def apply(self, state_slice) -> None:
        item = state_slice[ItemModel.fqdn]
        item[self.owner].intact -= 50