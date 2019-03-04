from typing import *

author = "Michael Yoo <michael@yoo.id.au>"


def pacman(input_file: str):
    """
    A wrapper around pacman_args.

    :param input_file: Filename of the input to parse
    :return: A 3-valued tuple (final_pos_x, final_pos_y, coins_collected)
    """
    with open(input_file) as f:
        input_str = f.read()

    # Normalise whitespace separator
    input_str = input_str.replace("\r\n", "\n")
    input_str = input_str.replace("\n", " ")
    input_str = input_str.split(" ")
    input_str = list(filter(lambda x: x != "", input_str))

    # Define initial values
    try:
        board_dimension = (int(input_str[0], base=10), int(input_str[1], base=10))
        initial_position = (int(input_str[2], base=10), int(input_str[3], base=10))
        movements = input_str[4]
        walls = map(
            lambda x: (int(x[0], base=10), int(x[1], base=10)),
            zip(input_str[5::2], input_str[6::2])
        )
        walls_dict = {}
        for wall_pos in walls:
            walls_dict[wall_pos] = True
    except (ValueError, IndexError):
        return -1, -1, 0

    return pacman_args(board_dimension, initial_position, movements, walls_dict)


def pacman_args(board_dimension: (int, int),
                initial_position: (int, int),
                movements: str,
                walls: Dict[(int, int)]) -> (int, int, int):
    """
    Perform a simulation of the PACMAN task.

    Assumptions made:
    - PACMAN cannot move beyond the boundaries of the board, otherwise it is an error
    -

    :param board_dimension: Dimensions of the board - e.g. (5, 5) for a 5x5 board
    :param initial_position: Initial position of PACMAN e.g. (0, 0) for bottom left
    :param movements: A string sequence of movements where c in "NESW"
    :param walls: A dictionary with wall coordinates as keys
    :return: A 3-valued tuple (final_pos_x, final_pos_y, coins_collected)
    """
    # Verify arguments
    if board_dimension[0] <= 0 or board_dimension[1] <= 0:
        return -1, -1, 0
    if not (0 <= initial_position[0] < board_dimension[0]) \
            or not (0 <= initial_position[1] < board_dimension[1]):
        return -1, -1, 0
    for move in movements:
        if not (move == "N" or move == "E" or move == "S" or move == "W"):
            return -1, -1, 0
    for wall_pos in walls.keys():
        if not (0 <= wall_pos[0] < board_dimension[0]) \
                or not (0 <= wall_pos[1] < board_dimension[1]):
            return -1, -1, 0

    # Start simulation
    visited = {initial_position: True}
    current_pos = initial_position
    coins_collected = 0

    for move in movements:
        if move == "N":
            attempt_pos = (current_pos[0], current_pos[1] + 1)
        elif move == "E":
            attempt_pos = (current_pos[0] + 1, current_pos[1])
        elif move == "S":
            attempt_pos = (current_pos[0], current_pos[1] - 1)
        elif move == "W":
            attempt_pos = (current_pos[0] - 1, current_pos[1])
        else:
            return -1, -1, 0

        # Attempted movement is out of bounds
        if not (0 <= attempt_pos[0] < board_dimension[0]) \
                or not (0 <= attempt_pos[1] < board_dimension[1]):
            return -1, -1, 0

        if attempt_pos not in walls:
            current_pos = attempt_pos

            if current_pos not in visited:
                visited[current_pos] = True
                coins_collected += 1

    return current_pos[0], current_pos[1], coins_collected


# Could use a testing framework here like hypothesis, but in the interest of time...
if __name__ == "__main__":
    assert pacman("test0.txt") == (1, 4, 7)
    assert pacman("test1.txt") != (-1, -1, 0)
    assert pacman("test2.txt") == (-1, -1, 0)
    assert pacman("test3.txt") == (0, 0, 15)
    assert pacman("test4.txt") == (-1, -1, 0)
    assert pacman("test5.txt") == (-1, -1, 0)
    assert pacman("test6.txt") == (9, 0, 9)
    assert pacman("test7.txt") == (3, 1, 6)
    assert pacman("test8.txt") == (1, 4, 7)
