from __future__ import annotations
from dataclasses import dataclass
from plug.abstract import Transform
from typing import Set

from dread_snarfle.model import PlayerModel
from dread_snarfle.error import PlaceholderError


@dataclass
class AssignPlayer(Transform):
    fqdn = 'dread_snarfle.transform.AssignPlayer'
    player: str = None
    name: str = None

    def required_authorizations(self) -> Set[str]:
        return {}

    @staticmethod
    def required_models() -> Set[str]:
        return {
            PlayerModel.fqdn,
        }

    def required_keys(self) -> Set[str]:
        return {
            self.player,
        }

    @staticmethod
    def pack(registry, obj) -> dict:
        return {
            'player': obj.player,
        }

    @classmethod
    def unpack(cls, registry, payload) -> 'AssignPlayer':
        return cls(
            player=payload['player'],
            model=payload['model'],
        )

    def verify(self, state_slice) -> None:
        if self.model is not None:
            raise PlaceholderError('Already has an associated player model!')

    def apply(self, state_slice) -> None:
        players = state_slice[PlayerModel.fqdn]
        players.append(PlayerModel(
            intact=100,
            name=self.name
        ))
