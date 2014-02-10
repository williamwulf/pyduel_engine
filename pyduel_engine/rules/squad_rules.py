
from pyduel_engine.content.engine_states import Cards

def are_minors_dead(squad):
    """is/are minor character(s) dead"""
    hp = 0
    for char in squad['characters']:
        if not char['is_main']:
            hp += char['hp']
    return hp == 0


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
    return can_act(squad) and has_hand(squad)


def can_heal_main(squad):
    """Can heal minor character. main must be dead and must have main card"""
    return can_act(squad) and are_minors_dead(squad) and has_minor_card(squad)


def can_heal_minor(squad):
    """Can heal minor character. main must be dead and must have main card"""
    return can_act(squad) and is_main_dead(squad) and has_main_card(squad)


def character_has_card(squad, character, card_types):
    """
    check if character has card in hand of the list of card_types
    can check to see if character can attack, defend, use special, or heal
    """
    if has_hand(squad):
        for card in squad['hand']:
            if card['owner'] == character[character] and \
                    (card['type'] == Cards.combat or
                     card['type'] == Cards.power_attack or
                     card['type'] == Cards.power_combat):
                        return True
    return False


def has_hand(squad):
    """Does squad have any cards in hand return boolean"""
    return len(squad['hand']) > 0


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
    #TODO: think of best way to account for different subcharacters
    """
    if has_hand(squad):
        for character in squad['characters']:
            if character['is_main']:
                for card in squad['hand']:
                    if card['owner'] != character['type']:
                        return True
    return False


def has_special_card(squad):
    pass


def is_main_dead(squad):
    """is main character dead"""
    # hp = 0
    # for char in squad['characters']:
    #     if not char['is_main']:
    #         hp += char['hp']
    # return hp == 0
    pass




