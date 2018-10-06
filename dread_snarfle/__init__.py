from plug.abstract import Plugin

import dread_snarfle.error
import dread_snarfle.model
import dread_snarfle.transform

class DreadSnarflePlugin(Plugin):
    @classmethod
    def setup(cls, registry) -> None:
        components = [
            dread_snarfle.error.PlaceholderError,
            dread_snarfle.model.CreatureModel,
            dread_snarfle.model.ItemModel,
            dread_snarfle.transform.CreatureEncounter,
        ]

        for component in components:
            registry.register(component)
