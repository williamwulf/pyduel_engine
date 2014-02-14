__author__ = 'aelkikhia'

from pyduel_engine.content.engine_states import Square as State
from pyduel_engine.content.engine_states import Boards as Bs


def place_character(board, character, pos):
    """Initial placement of character on board, or ignore move requirements
     and place character
    :param board: dictionary
    :param character: dictionary
    :param pos: dictionary
    :return:
    """
    pass


def place_multiple_characters(board, characters):
    """Initial placement of character on board, or ignore move requirements
     and place characters
    :param board:
    :param characters:
    """
    pass


def move_character(board, character, new_pos):
    """Move character on the board, update character dictionary with new
    coordinates
    :param board: dictionary
    :param character: dictionary
    :param new_pos: dictionary
    """
    pass


def move_multiple_characters(board, characters):
    """Move multiple characters"""
    #TODO: structure for list of characters and new positions
    pass


def remove_character(board, character):
    """Remove Character from board
    :param board: dictionary
    :param character: dictionary
    """
    pass


def remove_multiple_characters(board, characters):
    """Remove Character from board
    :param board: dictionary
    :param character: dictionary
    """
    pass


def initialize_board(board_type=None):
    """Builds board, sets all coordinates to empty
    :param board_type:
    :return:
    """
    return {'board_type': Bs.board, 'max_x': 10, 'max_y': 7,
            'board': [[State.empty for y in range(0, 7)]
                      for x in range(0, 10)]}