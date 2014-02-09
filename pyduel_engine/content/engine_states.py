__author__ = 'aelkikhia'

from enum import Enum


class SquareState(Enum):
    """
    Base Square States
    """
    empty = 0
    dark = 1
    light = 2
    obstacle = 3
    hole = 4


class Rolls(Enum):
    """
    Dice Sides
    """
    TWO_ALL = 0
    THREE = 1
    THREE_ALL = 2
    FOUR = 3
    FOUR_ALL = 4
    FIVE = 5