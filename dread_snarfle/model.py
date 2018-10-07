from __future__ import annotations
from dataclasses import dataclass
from plug.abstract import Model


@dataclass
class ItemModel(Model):
    fqdn = 'dread_snarfle.model.ItemModel'
    intact: int = 0
    name: str = None
    names: list = None
    repairs: dict = None
    qualities: dict = None

    @classmethod
    def default_factory(cls) -> 'ItemModel':
        return cls(
            intact=100
        )

    @staticmethod
    def pack(registry, obj) -> dict:
        return {
            'intact': obj.intact,
            'name': obj.name,
            'names': obj.names,
            'repairs': obj.repairs,
            'qualities': obj.qualities,
        }

    @classmethod
    def unpack(cls, registry, payload) -> 'ItemModel':
        return cls(
            intact=payload['intact'],
            name=payload['name'],
            names=payload['names'],
            repairs=payload['repairs'],
            qualities=payload['qualities'],
        )


@dataclass
class CreatureModel(Model):
    fqdn = 'dread_snarfle.model.CreatureModel'
    intact: int = 0
    name: str = None

    @classmethod
    def default_factory(cls) -> 'CreatureModel':
        return cls(
            intact=100
        )

    @staticmethod
    def pack(registry, obj) -> dict:
        return {
            'intact': obj.intact,
            'name': obj.name,
        }

    @classmethod
    def unpack(cls, registry, payload) -> 'CreatureModel':
        return cls(
            intact=payload['intact'],
            name=payload['name'],
        )


@dataclass
class PlayerModel(Model):
    fqdn = 'dread_snarfle.model.PlayerModel'
    intact: int = 0
    item: str = None
    model: str = None
    name: str = None

    @classmethod
    def default_factory(cls, registry, payload) -> 'PlayerModel':
        return cls(
            intact=payload['intact'],
            item=payload['item'],
            model=payload['model'],
            name=payload['name'],
        )

    @staticmethod
    def pack(registry, obj) -> dict:
        return {
            'intact': obj.intact,
            'item': obj.item,
            'model': obj.model,
            'name': obj.name,
        }

    @classmethod
    def unpack(cls, registry, payload) -> 'PlayerModel':
        return cls(
            intact=payload['intact'],
            item=payload['item'],
            model=payload['model'],
            name=payload['name'],
        )
