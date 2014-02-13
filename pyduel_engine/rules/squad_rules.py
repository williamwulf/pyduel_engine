"""
squad_rules.py is a collection of methods for validating actions according to
the default game rules of the duel engine

JSON FORMAT FOR A SQUAD
squad = {'player': <int>,
         'characters': [<list of characters>],
         'actions': <int>,
         'deck': [<list of cards>],
         'hand': [<list of cards>],
         'discard': [<list of cards>],
         'side': <enum>}

JSON FORMAT FOR A CHARACTER
main_character = {'name': <string>,
                    'hp': <int>,
                    'is_main': <boolean>,
                    'max_hp': <int>,
                    'type': <enum>,
                    'state': <enum>,
                    'pos': {'x': <int>, 'y': <int>,
                    'is_range': <boolean>,
                    'deck': [<list of cards>]}
"""

from pyduel_engine.rules import card_rules as cr
from pyduel_engine.content.engine_states import Cards


def are_minors_dead(squad):
    """is/are minor character(s) dead"""
    return sum([char['hp'] for char in squad['characters']
                if not char['is_main']]) == 0


def can_act(squad):
    """
    can squad do action
    """
    return squad['actions'] > 0


def can_attack(squad):
    pass


def can_use_special(squad):
    pass


def can_draw_card(squad):
    """check if squad can act and if they are able to draw a card"""
    return can_act(squad) and squad['can_draw']


def can_play_card(squad):
    """can squad play card"""
    return can_act(squad) and cr.has_hand(squad)


def can_heal_main(squad):
    """Can heal minor character. main must be dead and must have main card"""
    return can_act(squad) and are_minors_dead(squad) \
        and cr.has_minor_card(squad)


def can_heal_minor(squad):
    """Can heal minor character. main must be dead and must have main card"""
    return can_act(squad) and is_main_dead(squad) and cr.has_main_card(squad)


def character_has_card(squad, character, card_types):
    """
    check if character has card in hand of the list of card_types
    can check to see if character can attack, defend, use special, or heal
    """
    if cr.has_hand(squad):
        for card in squad['hand']:
            if card['owner'] == character[character] and \
                    (card['type'] == Cards.combat or
                     card['type'] == Cards.power_attack or
                     card['type'] == Cards.power_combat):
                        return True
    return False





def is_main_dead(squad):
    """is main character dead"""
    return sum([char['hp'] for char in squad['characters']
                if char['is_main']]) == 0




