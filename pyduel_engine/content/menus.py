

MOVE_MENU = {'question': 'Move to Square:',
             'choices': None}

ACTION_MENU = {'question': 'Choose an action:',
               'choices': ['Draw', 'Attack', 'Heal']}


START_MENU = {'question': 'Welcome to Star Wars Epic Duels:',
              'choices': ['Start Game', 'Load Game', 'Play Online']}

CHOOSE_NUM_PLAYERS = {'question': 'Number of players:',
                      'choices': range(1, 7)}

CHOOSE_PLAYER_SIDE = {'question': 'Choose Side:', 'choices': ['Light', 'Dark']}

CHOOSE_SQUAD = {'question': 'Choose Character:',
                'choices': [{'type': char['type'], 'choice': char['name']}
                            for char in CS.CHARACTERS.itervalues()
                            if char['is_main']]}

CHOOSE_BOARD = {'question': 'Choose Character:',
                'choices': [{'type': board['type'], 'choice': board['name']}
                            for board in BS.BOARDS.itervalues()]}
