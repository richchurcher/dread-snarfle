from plug.abstract import Plugin

import dread_snarfle.error
#  import free_money.error
#  import free_money.model
#  import free_money.transform

class FreeMoneyPlugin(Plugin):
    @classmethod
    def setup(cls, registry):
        components = [
            dread_snarfle.error.PlaceholderError,
        ]

        for component in components:
            registry.register(component)
