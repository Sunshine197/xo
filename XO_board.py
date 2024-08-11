import enum


class GameState(enum.Enum):
    X_WON = 1
    O_WON = 2
    DRAW = 3
    IN_PROGRESS = 4


board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


# This function is used to make a move on the board
def move(x, y, symbol):
    if 0 <= x < 3 and 0 <= y < 3 and board[x][y] == '-':
        board[x][y] = symbol
        return True
    return False


def what_is_the_game_state():
    # Check if someone won in the rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '-':
            return GameState.X_WON if board[i][0] == 'X' else GameState.O_WON

    # Check if someone won in the columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '-':
            return GameState.X_WON if board[0][i] == 'X' else GameState.O_WON

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return GameState.X_WON if board[0][0] == 'X' else GameState.O_WON
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return GameState.X_WON if board[0][2] == 'X' else GameState.O_WON

    return GameState.IN_PROGRESS


def __print_board():
    for row in board:
        print(' '.join(row))
