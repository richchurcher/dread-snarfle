from __future__ import annotations
from dataclasses import dataclass
from plug.abstract import Model


@dataclass
class ItemModel(Model):
    fqdn = 'dread_snarfle.model.ItemModel'
    intact: int
    name: str
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
    intact: int
    name: str

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
    intact: int
    name: str
    email: str

    @classmethod
    def default_factory(cls, registry, payload) -> 'PlayerModel':
        return cls(
            intact=payload['intact'],
            name=payload['name'],
            email=payload['email']
        )

    @staticmethod
    def pack(registry, obj) -> dict:
        return {
            'intact': obj.intact,
            'name': obj.name,
            'email': obj.email,
        }

    @classmethod
    def unpack(cls, registry, payload) -> 'PlayerModel':
        return cls(
            intact=payload['intact'],
            name=payload['name'],
            email=payload['email'],
        )
