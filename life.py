import argparse
import os
import random
import time


def get_arguments():
    parser = argparse.ArgumentParser()

    size = os.get_terminal_size()
    parser.add_argument(
        '-x',
        '--width',
        default=size.columns - 2,
        type=int,
        help='Board width.'
    )
    parser.add_argument(
        '-y',
        '--height',
        default=size.lines - 3,
        type=int,
        help='Board height.'
    )
    parser.add_argument(
        '-p',
        '--life-percentage',
        default=50,
        type=int,
        help = ('Percentage chance of cells ititializing alive. '
                'Only integers are allowed, and defaults to 50.')
    )
    parser.add_argument(
        '-f',
        '--file',
        metavar='FILE',
        help='Load initial state from a file.'
    )
    parser.add_argument(
        '-i',
        '--interval',
        default=0.1,
        type=float,
        help='Time interval in seconds between states.'
    )

    return parser.parse_args()


def load_initial_state(path):
    board = []

    with open(path, 'r') as f:
        for line in f.readlines():
            row = []
            for x in line:
                if x != "\n":
                    row.append(int(x))
            board.append(row)

    return board



def dead_state(width, height):
    board = list()
    while height > 0:
        row = list()
        i = width 
        while i > 0:
            row.append(0)
            i -= 1
        board.append(row)
        height -= 1

    return board


def random_state(board, life_percentage):
    y = len(board) - 1
    while y >= 0:
        x = len(board[y]) - 1
        while x >= 0:
            board[y][x] = dead_or_alive(life_percentage)
            x -= 1
        y -= 1

    return board


def dead_or_alive(life_percentage):
    number = random.random()
    if number > life_percentage:
        return 0
    else:
        return 1


def render(
        board_state,
        live_char='#',
        dead_char=' '
    ):
    columns = len(board_state[0])
    line = " " + "-" * columns
    
    output = line + "\n"
    
    for row in board_state:
        output += "|"
        for cell in row:
            if cell == 0:
                state = dead_char
            else:
                state = live_char

            output += state
        output += "|\n"

    output += line
    return output


def next_board_state(board):
    y = len(board)
    x = len(board[0])
    new_board = list()
    i = 0
    while i < y:
        new_row = []
        j = 0
        while j < x:
            new_state = next_cell_state(board, i, j)
            new_row.append(new_state)
            j += 1

        new_board.append(new_row)
        i += 1

    return new_board


def next_cell_state(board, row, cell):
    first_row = row == 0
    last_row = row == len(board) - 1
    first_cell = cell == 0
    last_cell = cell == len(board[row]) - 1
    live_neighbors = 0
    
    if not first_row:
        live_neighbors += board[row - 1][cell]
        if not first_cell:
            live_neighbors += board[row - 1][cell - 1]
        if not last_cell:
            live_neighbors += board[row - 1][cell + 1]

    if not first_cell:
        live_neighbors += board[row][cell - 1]

    if not last_cell:
        live_neighbors += board[row][cell + 1]

    if not last_row:
        live_neighbors += board[row + 1][cell]
        if not first_cell:
            live_neighbors += board[row + 1][cell - 1]
        if not last_cell:
            live_neighbors += board[row + 1][cell + 1]

    state = board[row][cell]
    new_state = calc_state(state, live_neighbors)

    return new_state


def calc_state(state, live_neighbors):
    if live_neighbors == 0 or live_neighbors == 1:
        return 0
    elif state == 1:
        if live_neighbors <= 3:
            return 1
        else:
            return 0
    elif live_neighbors == 3:
        return 1
    else:
        return 0


def run_life(board, interval):
    new_board = next_board_state(board)

    while new_board != board:
        rendered = render(new_board, live_char="•")
        print(rendered)
        time.sleep(interval)
        board = new_board
        new_board = next_board_state(new_board)


def main():
    args = get_arguments()

    if args.file:
        initial_state = load_initial_state(args.file)
    else:
        width = args.width
        height = args.height
        dead_state_board = dead_state(width, height)

        life_percentage = args.life_percentage / 100
        random_state_board = random_state(dead_state_board, life_percentage)
        initial_state = random_state_board

    run_life(initial_state, args.interval)


if __name__ == "__main__":
    main()
