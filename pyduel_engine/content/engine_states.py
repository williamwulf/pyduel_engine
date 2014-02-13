__author__ = 'aelkikhia'

from enum import Enum


class SquareState(Enum):
    """Base Square States"""
    empty = 0
    dark = 1
    light = 2
    obstacle = 3
    hole = 4


class Rolls(Enum):
    """Dice Sides"""
    two_all = 0
    three = 1
    three_all = 2
    four = 3
    four_all = 4
    five = 5


class Actions(Enum):
    """Squad Actions"""
    draw = 0
    attack = 1
    special = 2
    power_attack = 3
    heal_main = 5
    heal_minor = 6


class Cards(Enum):
    """Card Types"""
    combat = 0
    special = 1
    power_attack = 2
    power_defense = 3
    power_combat = 4


#######################################################
########### Generic types for testing #################
#######################################################


class Character(Enum):
    """Base Square States"""
    main = 0
    minor_1 = 1
    minor_2 = 2


class Boards(Enum):
    """generic boards"""
    board = 0
