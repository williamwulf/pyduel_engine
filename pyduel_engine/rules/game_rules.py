
from random import shuffle

from pyduel_engine.content.engine_states import SquareState as Sq


def is_game_over(squads):
    """
    returns true if all main dark or light side characters are dead
    """
    return (sum([Character.hp for Character in characters if Character.is_main
            and Character.state == Sq.light] for characters in squads) == 0) \
        or (sum([Character.hp for Character in characters if Character.is_main
            and Character.state == Sq.dark] for characters in squads) == 0)


def play_order():
    pass


def use_actions(game):
    """
    calls choose action then uses returned action type as key to dictionary
    of action methods
    """
    # if game
    # action = AR.choose_action()
    pass


def place_squad_on_board():
    pass



