import click

from commands import create_creature, create_player
import encounter
from utils import get_api_client


@click.command()
@click.argument('arg')
def init(arg):
    client = get_api_client()
    #  if arg == 'balance_query':
    #      input_address = click.prompt("please enter a user address",)
    #      init_balance_query(client, input_address)
    #      return

    if arg == 'create_player':
        create_player()
        return

    if arg == 'create_creature':
        create_creature()
        return

    #  if arg == 'free_money':
    #      input_key = click.prompt("please enter a user signing key",)
    #      amount = click.prompt("please enter the amount",)
    #      init_free_money(client, input_key, amount)
    #      return
    #
    if arg == 'encounter':
        sender_input_key = click.prompt("Player key")
        receiver_address = click.prompt("Creature address")
        encounter(client, sender_input_key, receiver_address)
        return

    else:
        print('Huh?')


if __name__ == '__main__':
    init()
