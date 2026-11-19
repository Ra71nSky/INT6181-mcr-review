"""Tic-tac-toe console game (version 2).

INT6181 Applied Programming with Python - Lecture 10 Modern Code Review.

Two players take turns entering the row and column of the cell they want.
After every move the program checks for a winner and prints "Win!" or, once
all nine cells are full, "Tie!"; either way the final grid is printed and the
game ends.

Version 2 is the revision produced by the in-class code inspection. The
problems found in version 1 and their fixes are recorded in the review notes;
each fix is marked with a NOTE-id below.
"""

WINNING_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
)

EMPTY = ' '


def new_board():
    """Return an empty 3x3 board as a flat list of nine cells."""
    return [EMPTY] * 9


def print_board(board):
    """Print the board as a 3x3 grid."""
    line = '+---+---+---+'
    print()
    print(line)
    for row in range(3):
        print('| {} | {} | {} |'.format(*board[row * 3:row * 3 + 3]))
        print(line)


def is_win(board, mark):
    """Return True when mark fills one whole row, column or diagonal."""
    return any(all(board[i] == mark for i in line) for line in WINNING_LINES)


def read_coordinate(prompt):
    """Ask for one coordinate and return it as a 0-based index.

    Keeps asking until the input is a whole number from 1 to 3. (NOTE-1)
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print('  Please type a whole number from 1 to 3.')
            continue
        if not 1 <= value <= 3:
            print('  The number must be between 1 and 3.')
            continue
        return value - 1


def read_cell(board, mark):
    """Ask for a cell until the player names an empty one. (NOTE-2)"""
    while True:
        row = read_coordinate('Row (1-3): ')
        col = read_coordinate('Col (1-3): ')
        index = row * 3 + col
        if board[index] == EMPTY:
            return index
        print('  That cell is already taken. '
              'Player {} please choose an empty cell.'.format(mark))


def main():
    """Run one game of tic-tac-toe."""
    board = new_board()
    mark = 'X'
    for _turn in range(9):
        print_board(board)
        print('Player {}, your turn.'.format(mark))
        index = read_cell(board, mark)
        board[index] = mark
        if is_win(board, mark):
            print('Win!')
            print_board(board)
            return
        mark = 'O' if mark == 'X' else 'X'
    print('Tie!')
    print_board(board)


if __name__ == '__main__':      # NOTE-3: only run when executed as a script
    main()
