import game_ui
import XO_board

if __name__ == '__main__':
    game_board = XO_board.board
    player = 'O'
    while True:
        game_ui.print_game_board(game_board)

        x, y = game_ui.get_user_input()
        XO_board.move(x, y, player)

        game_state = XO_board.what_is_the_game_state()
        if game_state == XO_board.GameState.X_WON:
            print("X won!")
            break
        elif game_state == XO_board.GameState.O_WON:
            print("O won!")
            break
        elif game_state == XO_board.GameState.DRAW:
            print("It's a draw!")
            break

        player = 'X' if player == 'O' else 'O'

