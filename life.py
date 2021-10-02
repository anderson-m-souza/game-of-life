import argparse
import random


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-x',
        '--width',
        default=30,
        type=int,
        help='Board width.'
    )
    parser.add_argument(
        '-y',
        '--height',
        default=10,
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

    return parser.parse_args()


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
    print(line)
    
    for row in board_state:
        print("|", end="")
        for cell in row:
            if cell == 0:
                state = dead_char
            else:
                state = live_char

            print(state, end="")
        print("|", end="\n")

    print(line)


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


def main():
    args = get_arguments()

    width = args.width
    height = args.height
    dead_state_board = dead_state(width, height)

    life_percentage = args.life_percentage / 100
    random_state_board = random_state(dead_state_board, life_percentage)

    render(random_state_board)


if __name__ == "__main__":
    main()
