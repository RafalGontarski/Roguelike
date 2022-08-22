import util
import engine
import ui

width = 20
height = 20

def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {
        "player_icon" : "@",
        "player_start_x" : 1,
        "player_start_y" : 1,
        "player_health" : 5}
    return player


def main():
    player = create_player()
    board = engine.create_board(width, height)

    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
