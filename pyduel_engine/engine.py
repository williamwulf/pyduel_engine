__author__ = 'aelkikhia'

from pyduel_engine.actions import engine_actions as ea


class Engine(object):

    def __init__(self):
        """Initializer for Engine"""
        self.players = None
        self.num_sides = None
        self.board = None
        self.turn_number = None
        self.squads = None

    def start(self):
        """Start engine"""

        pass

    def stop(self):
        """Stop engine"""
        pass

    def load(self):
        """load engine state"""
        pass

    def resume(self):
        """Resume engine state"""
        pass

    def save(self):
        """save engine state"""
        pass

    def quit(self):
        """quit engine"""
        pass

    def add_player(self):
        """add player to game engine"""
        pass

    def remove_player(self):
        """remove player from engine"""
        pass

    def add_squad(self):
        """add squad to engine"""
        pass

    def remove_squad(self):
        """remove squad to engine"""
        pass

    def set_turn_number(self):
        """set turn number"""
        pass

if __name__ == '__main__':
    engine = Engine()
    print('We got an engine')