__author__ = 'aelkikhia'

from random import randrange
from random import shuffle

from pyduel_engine.rules import card_rules


def draw_card(squad):
    """draw card from deck"""
    squad['hand'].append(squad['deck'].pop())


def draw_cards(squad, num_cards):
    """all squads draw card"""
    for x in range(0, num_cards):
        draw_card(squad)


def deal_cards_to_squads(squads, num_cards=4):
    """Deals out hand to each squad Hand defaults to 4 to match an initial
    game start
    :param squads: (Dict)
    :param num_cards: (Int)
    """
    for squad in squads:
        draw_cards(squad, num_cards)


def discard_card(squad, card_index=None):
    """Discard a card. if card_index is None, discard random card"""
    if not card_index:
        card_index = randrange(0, len(squad))

    squad['discard'].append(choose_card(squad['hand'], card_index))


def discard_cards(squad, num_cards=None, card_indices=None):
    """discard multiple cards"""
    if num_cards:
        for _ in range(0, num_cards):
            discard_card(squad)
    elif card_indices:
        for index in sorted(card_indices, reverse=True):
            discard_card(squad, index)
    else:
        #todo: throw an exception
        pass


def shuffle_discard_into_deck(squad):
    """Inserts the discard list into the deck list and shuffles
    returns the squad dictionary
    :param squad:
    """
    squad['deck'].extend(squad['discard'])
    squad['discard'] = []
    squad['deck'] = shuffle(squad['deck'])


def main_cards(squad):
    """check hand for card belonging to main character"""
    # if has_hand(squad):
    #     for character in squad['characters']:
    #         if character['is_main']:
    #             for card in squad['hand']:
    #                 if card['owner'] == character['type']:
    #                     return True
    # return False
    pass


def choose_card(cards, index):
    """return card from list of cards """
    return cards.pop(index)


def attack():
    """Attack opponent"""
    pass


def special_attack():
    """Special Attack"""
    pass


def defense():
    """Attack opponent"""
    # pick_defense_card()
    pass


def special_defense():
    """Special Attack"""
    pass
