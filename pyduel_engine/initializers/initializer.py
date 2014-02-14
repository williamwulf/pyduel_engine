
# def character_initializer(character_type, position=None, side=None):
#     character = CS.CHARACTERS[character_type]
#     character['pos'] = position
#     character['side'] = side
#     character['deck'] = build_character_deck(character['deck'],
#                                              character_type)
#     return character
#
#
# def setup_squad(player_number, character, side):
#     squad = {'player': player_number,
#              'characters': number_secondary_characters(set_squad_side(
#                  CS.SQUADS[character], side)),
#              'actions': 2,
#              'deck': build_squad_deck(CS.SQUADS[character]),
#              'hand': [],
#              'discard': [],
#              'side': side}
#     return squad
#
#
# def _build_board(max_x=10, max_y=7):
#     return [[GS.EMPTY for y in range(max_y)] for x in range(max_x)]


# def board_initializer(board_type):
#     """
#     builds board by adding holes, obstructions
#     """
#     board = _build_board()
#
#     # Json board coordinates
#     for square_states in BS.BOARDS[board_type]['states']:
#         for pos in BS.BOARDS[board_type]['states'][square_states]:
#             board[pos['x']][pos['y']] = square_states
#     return {'board_type': board_type, 'max_x': 10, 'max_y': 7,'board': board}


def set_squad_side(squad, side):
    """
    creates deck for squad
    """
    for character in squad:
        character['state'] = side
    return squad


def build_squad_deck(squad):
    """
    creates deck for squad
    """
    deck = []
    for character in squad:
        deck += character['deck']
    return deck


def build_character_deck(deck, owner):
    """
    sets owner to deck of cards
    """
    for card in deck:
        card['owner'] = owner
    return deck


# def game_initializer(board_type):
#     return {'squads': [],
#             'round': 1,
#             'turn': None,
#             'board': board_initializer(board_type)}


def number_secondary_characters(characters):
    number = 1
    for char in characters:
        if not char['is_main']:
            char['number'] = number
            number += 1
    return characters
