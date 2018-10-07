from asyncio import get_event_loop

from client.utils import register_transform_event
from dread_snarfle.creature_encounter import CreatureEncounter


def encounter(client, player, creature):
    register_transform_event(CreatureEncounter)

    loop = get_event_loop()

    response = loop.run_until_complete(client.broadcast_transform(CreatureEncounter(
        player=player,
        creature=creature
    )))

    print(response)
