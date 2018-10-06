from plug.abstract import Plugin

import dread_snarfle.error
import dread_snarfle.model
from dread_snarfle.creature_encounter import CreatureEncounter


class GamePlugin(Plugin):
    @classmethod
    def setup(cls, registry) -> None:
        components = [
            dread_snarfle.error.PlaceholderError,
            dread_snarfle.model.CreatureModel,
            dread_snarfle.model.ItemModel,
            dread_snarfle.model.PlayerModel,
            CreatureEncounter,
        ]

        for component in components:
            registry.register(component)
