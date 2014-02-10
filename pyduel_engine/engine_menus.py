__author__ = 'aelkikhia'

from pyduel_engine.content import menus
from pyduel_engine.model.menu import MenuLoader as menu_loader


def move_character(board, moves, char_pos):
    """
    move character from current position to new position
    """
    # move_menu = menus.MOVE_MENU
    # move_menu['choices'] = BR.find_moves(board, moves, char_pos)
    #
    # menu = menu_loader(move_menu)
    # choice = menu.load_menu()
    # return choice
    pass


def choose_number_of_players(choice=None):
    if not choice:
        menu = menu_loader(menus.CHOOSE_NUM_PLAYERS)
        return menu.load_menu()
    return choice


def choose_player_sides(choice=None):
    if not choice:
        menu = menu_loader(menus.CHOOSE_PLAYER_SIDE)
        return menu.load_menu()
    return choice


def choose_players_squads(choice=None):
    if not choice:
        menu = menu_loader(menus.CHOOSE_SQUAD)
        return menu.load_enum_menu()
    return choice


def choose_game_board(choice=None):
    if not choice:
        menu = menu_loader(menus.CHOOSE_BOARD)
        choice = menu.load_enum_menu()
    return choice


def initialize_player_squads(num_players):
    # squads = []
    # for player_number in range(0, num_players+1):
    #     squads.append(init.setup_squad(player_number,
    #                                    choose_players_squads(),
    #                                    choose_player_sides()))
    # return squads
    pass
