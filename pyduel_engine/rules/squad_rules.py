"""
squad_rules.py is a collection of methods for validating actions according to
the default game rules of the duel engine

JSON FORMAT FOR A SQUAD
squad = {'player': <int>,
         'characters': [<list of characters>],
         'actions': <int>,
         'can_draw': boolean,
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

COMBAT_5_1 = {'type': COMBAT, 'name': 'combat', 'attack': 5, 'defense': 1,
'owner': '', 'description': ''}
"""

from pyduel_engine.content.engine_states import Cards


###################### Actions ######################################

def can_act(squad):
    """can squad perform any actions"""
    return squad['actions'] > 0


def can_draw_card(squad):
    """check if squad can act and if they are able to draw a card"""
    return can_act(squad) and squad['can_draw']


def can_play_card(squad):
    """can squad play card"""
    return can_act(squad) and has_hand(squad)


def can_heal_main(squad):
    """Can heal minor character. main must be dead and must have main card"""
    return are_minors_dead(squad) and has_main_card(squad)


def can_heal_minor(squad):
    """Can heal minor character. main must be dead and must have main card"""
    return is_main_dead(squad) and has_minor_card(squad)


###################### Character ######################################

# def can_heal(squad, character):
#     """check if character can heal"""
#     return sum([char['hp'] for char in squad['characters']
#                 if not character['is_main']]) == 0


def are_minors_dead(squad):
    """is/are minor character(s) dead"""
    return sum([char['hp'] for char in squad['characters']
                if not char['is_main']]) == 0


def is_main_dead(squad):
    """is main character dead"""
    print([char['hp'] for char in squad['characters'] if char['is_main']])
    return sum([char['hp'] for char in squad['characters']
                if char['is_main']]) == 0


############################ Hand ###################################


def has_hand(squad):
    """Does squad have any cards in hand return boolean"""
    return len(squad['hand']) > 0


def character_has_card(squad, character, card_types=None):
    """check if character has card in hand of the list of card_types can
    check to see if character can attack, defend, use special, or heal
    :param squad: dictionary
    :param character: character type to associate with cards in hand
    :param card_types: list of card types
    :return: boolean
    """
    # does squad have a hand
    if has_hand(squad):
        # get list of characters cards
        cards = [card for card in squad['hand']
                 if card['owner'] == character['type']]
        # if card type specified return total number of cards belonging to char
        if card_types:
            return sum([card for card in cards
                        if card['type'] in card_types]) > 0
        # if no card type is specified
        return len(cards) > 0
    return False


def has_attack_card(squad, character):
    """Check if squad has any remaining actions
    :param squad: dictionary
    :param character: character
    :return: boolean
    """
    types = [Cards.combat, Cards.power_attack, Cards.power_combat]
    return character_has_card(squad, character, types)


def has_defense_card(squad, character):
    """Check if squad has any remaining actions
    :param squad: dictionary
    :param character: character
    :return: boolean
    """
    types = [Cards.combat, Cards.power_defense, Cards.power_combat]
    return character_has_card(squad, character, types)


def has_special_card(squad, character):
    """check if character has special card
    :param squad: dictionary
    :param character: character type
    :return: return boolean
    """
    return character_has_card(squad, character, [Cards.special])


def has_main_card(squad):
    """check hand for card belonging to main character"""
    if has_hand(squad):
        for character in squad['characters']:
            if character['is_main']:
                for card in squad['hand']:
                    if card['owner'] == character['type']:
                        return True
    return False


def has_minor_card(squad):
    """check hand for card belonging to minor character
    #TODO: think of best way to account for different sub characters
    """
    if has_hand(squad):
        for character in squad['characters']:
            if character['is_main']:
                for card in squad['hand']:
                    if card['owner'] != character['type']:
                        return True
    return False

