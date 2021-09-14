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
