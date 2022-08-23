from time import sleep
import util
import engine
import ui

width = 10
height = 10

def create_player():
    player = {
        "player_icon" : "@",
        "x" : 1,
        "y" : 1,
        "player_health" : 5}
    return player

def main():
    player = create_player()
    board = engine.create_board(width, height)
    items = ['*', '/', '^', '$']
    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)
        engine.remove_player_from_board(board, player)

        key = util.key_pressed()
        field = engine.player_movement(key, board, player)
        if field in items:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
