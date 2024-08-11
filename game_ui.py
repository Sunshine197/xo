def print_game_board(board):
    print("  0 1 2")
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(board[i][j], end=" ")
        print()


def get_user_input():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    return x, y