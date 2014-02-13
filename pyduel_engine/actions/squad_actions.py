__author__ = 'aelkikhia'

from pyduel_engine.rules import squad_rules
from pyduel_engine.content.engine_states import Actions
from pyduel_engine.actions import card_actions as ca


def squad_draw_card(squad):
    if squad_rules.can_draw_card(squad):
        ca.draw_card(squad)


def play_card():
    """Play card"""
    pass


def choose_defense_card():
    pass


def choose_attack_card():
    pass


def choose_special_card():
    pass


def change_character_hp(character, value):
    """modify character hp"""
    pass


def choose_action(squad):
    """choose squad action"""
    # actions = get_available_actions(squad)
    pass


def discard_to_heal(squad, character, index):
    """action discard card to heal"""
    # if minors_dead(squad) and has_minor_card(squad):
    #     discard_card(squad, index)
    #     for character in squad['characters']:
    #         if character['is_main']:
    #             character['hp'] += 1
    pass


def get_available_actions(squad):
    """get dictionary of all available actions"""
    # TODO: return dictionary of all character and squad actions
    # available_actions = {}
    # if squad_rules.can_draw_card(squad):
    #     available_actions.append(Actions.draw)
    # if squad_rules.can_heal_minor(squad):
    #     available_actions.append(Actions.heal_minor)
    # if squad_rules.can_heal_main(squad):
    #     available_actions.append(Actions.heal_main)
    # if squad_rules.can_attack(squad):
    #     available_actions.append(Actions.attack)
    # if squad_rules.can_use_special(squad):
    #     available_actions.append(Actions.special)
    #
    # return available_actions
    pass


