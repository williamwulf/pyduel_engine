__author__ = 'aelkikhia'


def roll():
    """Roll Dice"""
    pass


def move_character(character):
    """Move character"""
    pass


def move_squad(squad):
    """move squad"""
    for character in squad:
        move_character(character)


def actions():
    """squad perform actions"""
    pass


def turn(squad):
    """squad turn"""
    roll()
    move_squad(squad)
    actions()


def set_squad_side(squad, state):
    """Set what side the squad"""
    squad['side'] = state


def setup_engine():
    pass




