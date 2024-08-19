import enum


class GameState(enum.Enum):
    X_WON = 1
    O_WON = 2
    DRAW = 3
    IN_PROGRESS = 4

board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

def move(x, y, player):
    if x < 0 or x > 2 or y < 0 or y > 2:
        return False

    board[x][y] = player
    return True

def what_is_the_game_state():
    for i in range(3):
        # check rows
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '-':
            return 1 if board == 'X' else 2

        # check columns
        elif board[i][0] == board[i][1] == board[i][2] and board[i][0] != '-':
            return 1 if board == 'X' else 2

        # check diagonals
        elif board[i][i] == board[i][i + 1] == board[i][i + 2] and board[i][i] != '-':
            return 1 if board == 'X' else 2

        # check draw
        if "-" not in board:
            return 3

        else:
            return 4