__author__ = 'aelkikhia'


from math import fabs
from pyduel_engine.content.engine_states import Square as Sq


def square_state(board, pos):
    """Get square state from board"""
    return board['board'][pos['x']][pos['y']]


def is_diagonal(origin, target):
    """Verify if points are diagonal"""
    return fabs(origin['x'] - target['x']) == fabs(origin['y'] - target['y'])


# verify if positions are parallel
def is_parallel(origin, target):
    """Verify if points are parallel"""
    return origin['x'] == target['x'] or origin['y'] == target['y']


def is_adjacent(origin, target):
    """Verify if points are adjacent"""
    return ((origin['x'] == target['x'] and
             fabs(origin['y'] - target['y'])) == 1) or \
           ((origin['x'] == target['y'] and
             fabs(origin['x'] - target['x'])) == 1) or \
           ((origin['y'] == target['y'] and
             fabs(origin['x'] - target['x'])) == 1) or \
           ((is_diagonal(origin, target) and
             fabs(origin['x'] - target['x'])) == 1)


def _is_parallel_clear_x_axis(board, origin, target):
    """called if the pivot is on the x plane and traverses through all the
    squares to check if path is clear"""
    pivot = origin['x']
    if origin['y'] < target['y']:
        index = origin['y'] + 1
        end = target['y']
    else:
        index = target['y'] + 1
        end = origin['y']
    while index != end:
        if board[pivot][index] == Sq.empty or board[pivot][index] == Sq.hole:
            index += 1
        else:
            return False
    return True


def _is_parallel_clear_y_axis(board, origin, target):
    """called if the pivot is on the y plane and traverses through all the
    squares to check if path is clear"""
    pivot = origin['y']

    if origin['x'] < target['x']:
        index = origin['x'] + 1
        end = target['x']
    else:
        index = target['x'] + 1
        end = origin['x']
    while index != end:
        if board[index][pivot] == Sq.empty or board[index][pivot] == Sq.empty:
            index += 1
        else:
            return False
    return True


def is_parallel_clear(board, origin, target):
    """Verify if there is a clear parallel path between two points"""
    # not parallel, moot point
    if not is_parallel(origin, target):
        return False

    # if adjacent it's already a valid target
    if is_adjacent(origin, target):
        return True
    if origin['x'] == target['x']:
        # when x is the pivot
        return _is_parallel_clear_x_axis(board, origin, target)
    else:
        # when y is the pivot
        return _is_parallel_clear_y_axis(board, origin, target)


def is_diagonal_clear(board, origin, target):
    """Verify if there is a clear diagonal path between two points"""

    x, y = -1, -1
    end = int(fabs(origin['x'] - target['x']) - 1)

    # set modifiers for x and y coordinate traversal
    if origin['x'] < target['x']:
        x = 1

    if origin['y'] < target['y']:
        y = 1

    for i in range(1, end):
        if (board[origin['x'] + x * i][origin['y'] + y * i] != Sq.empty) and \
                (board[origin['x'] + x * i][origin['y'] + y * i] != Sq.hole):
            return False
    return True


def is_legal_target(char, target):
    """verify if legal target"""
    if not char['is_range'] and not is_adjacent(char['pos'], target['pos']):
        return False
    return char['state'] != target['state']


def can_range_attack(board, char, target):
    """Verify if target can be range attacked."""
    return is_legal_target(char, target) and is_diagonal_clear(board,
                                                               char['pos'],
                                                               target['pos'])


def can_melee_attack(char1, target):
    """verify if target can be melee attacked"""
    return is_legal_target(char1, target) and is_adjacent(char1['pos'],
                                                          target['pos'])


def get_all_adjacent_characters(chars, origin):
    """return list of adjacent characters (I love list comprehension)"""
    return [char for char in chars
            if is_adjacent(origin['pos'], char['pos'])]


def get_all_adjacent_friends(chars, origin):
    """return list of adjacent friendly characters (I love list comprehension)
    """
    return [char for char in chars
            if is_adjacent(origin['pos'], char['pos']) and
            not is_legal_target(origin, char)]


def get_all_adjacent_enemies(chars, origin):
    """return list of adjacent enemy characters (I love list comprehension)
    """
    return [char for char in chars
            if is_adjacent(origin['pos'], char['pos']) and
            is_legal_target(origin, char)]


def is_obstructed(board, pos):
    """Verify if a character can move through any of the adjacent squares"""
    return not can_move_through(board, pos, shift_down(pos)) and \
        not can_move_through(board, pos, shift_up(pos)) and \
        not can_move_through(board, pos, shift_left(pos)) and \
        not can_move_through(board, pos, shift_right(pos))


def is_out_of_bounds(board, pos):
    """check if square is out of bounds or not"""
    return pos['x'] >= board['max_x'] or pos['x'] < 0 or pos['y'] < 0 or \
        pos['y'] >= board['max_y']


def can_move_through(board, pos, new_pos):
    """verifies if a a square can be moved on or through"""
    return square_state(board, new_pos) == Sq.empty or \
        square_state(board, new_pos) == square_state(board, pos)


def is_valid_move(board, pos, new_pos):
    """check if is valid move"""
    return not is_out_of_bounds(board, new_pos) and pos != new_pos and \
        can_move_through(board, pos, new_pos)


def is_empty(board, pos):
    """make sure square is empty"""
    return square_state(board, pos) == Sq.empty


def shift_up(pos):
    """returns new position that has shifted up"""
    return {'x': pos['x'], 'y': pos['y'] + 1}


def shift_down(pos):
    """returns new position that has shifted down"""
    return {'x': pos['x'], 'y': pos['y'] - 1}


def shift_right(pos):
    """returns new position that has shifted right"""
    return {'x': pos['x'] + 1, 'y': pos['y']}


def shift_left(pos):
    """returns new position that has shifted left"""
    return {'x': pos['x'] - 1, 'y': pos['y']}


def find_moves(board, num_moves, old_pos, new_pos=None, possible_moves=None):

    # if this is the first call, set new position gets our current position
    # we can use the pos variable to make sure we don't backtrack,
    # also create possible_moves list
    if not new_pos:
        new_pos = old_pos
        possible_moves = []

    # if no num_moves
    if num_moves == -1:
        return possible_moves

    # decrement the number of moves
    num_moves -= 1

    # add
    if is_empty(board, new_pos):
        possible_moves.append(new_pos)

    # check up
    up = shift_up(new_pos)
    if is_valid_move(board, up, old_pos):
        find_moves(board, num_moves, new_pos, up, possible_moves)

    # check down
    down = shift_down(new_pos)
    if is_valid_move(board, up, old_pos):
        find_moves(board, num_moves, new_pos, down, possible_moves)

    # check left
    left = shift_left(new_pos)
    if is_valid_move(board, up, old_pos):
        find_moves(board, num_moves, new_pos, left, possible_moves)

    # check right
    right = shift_right(new_pos)
    if is_valid_move(board, up, old_pos):
        find_moves(board, num_moves, new_pos, right, possible_moves)


        #
        # def how_far_away_melee(board, char1, char2):
        #     """how many moves to get in melee attack range"""
        #     pass
        #
        #
        # def how_far_away_range(board, char1, char2):
        #     """how many moves to get in attack range"""
        #     pass



