from time import sleep
import util
import engine
import ui

width = 10
height = 10

def create_player():
    player = {
        "player_name" : "",
        "player_icon" : "@",
        "x" : 1,
        "y" : 1,
        "player_health" : 0,
        "player_attack": 0,
        "player_defense" : 0,
        "equipped_sword" : "",
        "equipped_helmet" : "",
        "equipped_armor" : "",
        "equipped_weapon2" : "",
        "equipped_potion" : "",
        }
    player["player_name"] = input('Player name: ').capitalize()
    while True:
        print('Type lists: Dwarf(1), Elves(2), Human(3)')
        type_lists = ("1", "2", "3")
        player_type = input("Please choose your type (1 or 2 or 3): ")
        if player_type not in type_lists:
            print("Wrong input, please choose 1, 2 or 3")
            continue
        else:
            break 
    if player_type == "1":
        player["player_health"] = 20
        player["player_attack"] = 3
        player["player_defense"] = 6
    elif player_type == "2":
        player["player_health"] = 14
        player["player_attack"] = 6
        player["player_defense"] = 3
    elif player_type == "3":
        player["player_health"] = 15
        player["player_attack"] = 4
        player["player_defense"] = 4 
    return player

def main():
    inventory = []
    position_list = []
    player = create_player()
    cpu_1 = engine.create_enemy(position_list)
    cpu_2 = engine.create_enemy_2(position_list)
    bread = engine.create_bread(position_list)
    wooden_helmet = engine.create_wooden_helmet(position_list)
    sword = engine.create_sword(position_list)
    board = engine.create_board(width, height)

    mobs = ['m', 'M']
    items = ['/','*','$','<','>','^','m','M']
    util.clear_screen()
    is_running = True
    engine.put_cpu1_on_board(board,cpu_1)
    engine.put_cpu2_on_board(board, cpu_2)
    engine.put_bread_on_board(board, bread)
    engine.put_helmet_on_board(board, wooden_helmet)
    engine.put_sword_on_board(board, sword)
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board,player,inventory)
        engine.remove_player_from_board(board, player)

        key = util.key_pressed()
        field = engine.player_movement(key, board, player,items)
        if field in items:
            engine.add_to_inventory(inventory, field, player)
        if field == 'm':
                engine.fight_with_NPC(cpu_1, player)
        elif field == 'M':
                engine.fight_with_NPC(cpu_2, player)
        if player['player_health'] <= 0:
            print("You have died!")
            sleep(3)
            break
        util.clear_screen()

if __name__ == '__main__':
    main()
