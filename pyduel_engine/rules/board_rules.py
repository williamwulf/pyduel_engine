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
    """Verify if a character can move through any of the adjacent squares
    """
    return \
        not can_move_through(board, pos,
                             {'x': pos['x'], 'y': pos['y'] - 1}) and \
        not can_move_through(board, pos,
                             {'x': pos['x'], 'y': pos['y'] + 1}) and \
        not can_move_through(board, pos,
                             {'x': pos['x'] - 1, 'y': pos['y']}) and \
        not can_move_through(board, pos, {'x': pos['x'] + 1, 'y': pos['y']})


def is_out_of_bounds(board, pos):
    """check if square is out of bounds or not
    """
    return pos['x'] >= board['max_x'] or pos['x'] < 0 or pos['y'] < 0 or \
        pos['y'] >= board['max_y']


def can_move_through(board, pos, new_pos):
    """verifies if a a square can be moved on or through
    """
    return square_state(board, new_pos) == Sq.empty or \
        square_state(board, new_pos) == square_state(board, pos)


def find_moves(board, num_moves, pos, new_pos=None, list_moves=None):
    # TODO: Make sense of all this and document it properly
    """returns list of all possible moves for a given character
    """
    if not new_pos:
        new_pos = pos

    if list_moves is None:
        list_moves = []

    if num_moves == -1:
        return [dict(t) for t in set([tuple(d.items()) for d in list_moves])]

    if is_out_of_bounds(board, pos) or is_obstructed(board, pos):
        return [dict(t) for t in set([tuple(d.items()) for d in list_moves])]

    num_moves -= 1

    list_moves.append(new_pos)

    if can_move_through(
            board, new_pos, {'x': new_pos['x'], 'y': new_pos['y'] - 1}) and \
            pos != {'x': new_pos['x'], 'y': new_pos['y'] - 1}:
        find_moves(board, num_moves, new_pos,
                   {'x': new_pos['x'], 'y': new_pos['y'] - 1}, list_moves)

    if can_move_through(
            board, new_pos, {'x': new_pos['x'], 'y': new_pos['y'] + 1}) and \
            pos != {'x': new_pos['x'], 'y': new_pos['y'] + 1}:
        find_moves(board, num_moves, new_pos,
                   {'x': new_pos['x'], 'y': new_pos['y'] + 1}, list_moves)

    if can_move_through(
            board, new_pos, {'x': new_pos['x'] - 1, 'y': new_pos['y']}) and \
            pos != {'x': new_pos['x'] - 1, 'y': new_pos['y']}:
        find_moves(board, num_moves,  new_pos,
                   {'x': new_pos['x'] - 1, 'y': new_pos['y']}, list_moves)

    if can_move_through(
            board, new_pos, {'x': new_pos['x'] + 1, 'y': new_pos['y']}) and \
            pos != {'x': new_pos['x'] + 1, 'y': new_pos['y']}:
        find_moves(board, num_moves, new_pos,
                   {'x': new_pos['x'] + 1, 'y': new_pos['y']}, list_moves)

    return [dict(t) for t in set([tuple(d.items()) for d in list_moves])]
