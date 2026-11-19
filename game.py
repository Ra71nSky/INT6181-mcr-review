# game.py - Tic-tac-toe
# INT6181 Applied Programming with Python - Lecture 10 Modern Code Review activity
# Author: Ra71nSky (student A)     Reviewers: R (student B) + GitHub Copilot (cyber reviewer AI)

board = [' '] * 9


def print_board():
    print()
    print('-------------')
    for r in range(3):
        print('| %s | %s | %s |' % (board[r*3], board[r*3+1], board[r*3+2]))
        print('-------------')


def is_win(p):
    return ((board[0] == p and board[1] == p and board[2] == p) or
            (board[3] == p and board[4] == p and board[5] == p) or
            (board[6] == p and board[7] == p and board[8] == p) or
            (board[0] == p and board[3] == p and board[6] == p) or
            (board[1] == p and board[4] == p and board[7] == p) or
            (board[2] == p and board[5] == p and board[8] == p) or
            (board[0] == p and board[4] == p and board[8] == p) or
            (board[2] == p and board[4] == p and board[6] == p))


def main():
    player = 'X'
    for turn in range(9):
        print_board()
        print('Player', player, 'turn.')
        row = int(input('Row (1-3): '))
        col = int(input('Col (1-3): '))
        board[(row - 1) * 3 + (col - 1)] = player
        if is_win(player):
            print('Win!')
            print_board()
            return
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
    print('Tie!')
    print_board()


main()
