__author__ = 'aelkikhia'


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
    #TODO: think of best way to account for different sub characters
    """
    if has_hand(squad):
        for character in squad['characters']:
            if character['is_main']:
                for card in squad['hand']:
                    if card['owner'] != character['type']:
                        return True
    return False