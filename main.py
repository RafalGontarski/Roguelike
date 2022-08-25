from time import sleep
import util
import engine
import ui
import walls, mobs

width = 25
height = 25

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
    cpu_1 = mobs.create_enemy_map1(position_list)
    cpu_2 = mobs.create_enemy2_map1(position_list)
    cpu_3 = mobs.create_enemy3_map1(position_list)
    cpu_4 = mobs.create_enemy4_map1(position_list)

    bread = engine.create_bread(position_list)
    wooden_helmet = engine.create_wooden_helmet(position_list)
    sword = engine.create_sword(position_list)
    board = engine.create_board(width, height)

    
    board2 =  engine.create_board(width, height)
    board3 = engine.create_board(width, height)
    board2[3][1] = "O"
    board3 = engine.create_board(width, height)
    walls.board1_walls(board)
    walls.board2_walls(board2)
    walls.board3_walls(board3)
    mobs.put_cpu1_on_board(board,cpu_1)
    mobs.put_cpu2_on_board(board,cpu_2)
    mobs.put_cpu3_on_board(board,cpu_3)
    mobs.put_cpu4_on_board(board,cpu_4)

    using_map = board

    items = ['/','*','$','<','>','^','m','M', 'O', 'g','G']
    
    engine.put_bread_on_board(board, bread)
    engine.put_helmet_on_board(board, wooden_helmet)
    engine.put_sword_on_board(board, sword)
    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(using_map, player)
        ui.display_board(using_map,player,inventory)
        engine.remove_player_from_board(using_map, player)

        key = util.key_pressed()
        field = engine.player_movement(key, using_map, player,items)
        if field in items:
            engine.add_to_inventory(inventory, field, player)
        if field == 'm':
            while cpu_1['cpu_health'] > 0:
                engine.fight_with_NPC(cpu_1, player)
                engine.player_death(player)
        elif field == 'M':
            while cpu_4['cpu_health'] > 0:
                engine.fight_with_NPC(cpu_4, player)
                engine.player_death(player)         
            else:
                using_map[1][1] = 'O'
        elif field == 'g':
            while cpu_2['cpu_health'] > 0:
                engine.fight_with_NPC(cpu_2, player)
                engine.player_death(player) 
        elif field == 'G':
            while cpu_3['cpu_health'] > 0:
                engine.fight_with_NPC(cpu_3, player)
                engine.player_death(player) 
        if field == 'O':
            player["x"] = 1
            player["y"] = 1
            
            if using_map == board:
                using_map = board2
                mobs.mob_max_hp(cpu_1)
                mobs.mob_max_hp(cpu_2)
                mobs.mob_max_hp(cpu_3)
                mobs.mob_max_hp(cpu_4)
                engine.bread_change_place(bread)
                engine.put_bread_on_board(board2,bread)
            elif using_map == board2:
                using_map = board3
                mobs.mob_max_hp(cpu_1)
                mobs.mob_max_hp(cpu_2)
                mobs.mob_max_hp(cpu_3)
                mobs.mob_max_hp(cpu_4)
                engine.bread_change2_place(bread)
                engine.put_bread_on_board(board3,bread)
        util.clear_screen()

if __name__ == '__main__':
    main()
