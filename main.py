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
        "player_health" : 5,
        "player_attack": 2,
        "player_defense" : 3}
    return player

def main():
    inventory = []
    position_list = []
    player = create_player()
    cpu_1 = engine.create_enemy(position_list)
    cpu_2 = engine.create_enemy_2(position_list)
    bread = engine.create_bread(position_list)
    helmet = engine.create_helmet(position_list)
    sword = engine.create_sword(position_list)
    board = engine.create_board(width, height)
    items = ['*', '/', '^', '$']
    util.clear_screen()
    is_running = True
    engine.put_cpu1_on_board(board,cpu_1)
    engine.put_cpu2_on_board(board, cpu_2)
    engine.put_bread_on_board(board, bread)
    engine.put_helmet_on_board(board, helmet)
    engine.put_sword_on_board(board, sword)
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board,player,inventory)
        engine.remove_player_from_board(board, player)

        key = util.key_pressed()
        field = engine.player_movement(key, board, player)
        if field in items:
            engine.add_to_inventory(inventory, field, player)  
        util.clear_screen()

if __name__ == '__main__':
    main()
