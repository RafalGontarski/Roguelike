import random
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
    boss = mobs.create_boss(position_list)
    steel_helmet = engine.create_steel_helmet(position_list)
    bread = engine.create_bread(position_list)
    wooden_helmet = engine.create_wooden_helmet(position_list)
    wooden_sword = engine.create_sword(position_list)
    steel_sword = engine.create_sword2(position_list)
    board = engine.create_board(width, height)
    
    
    board2 =  engine.create_board(width, height)
    board3 = engine.create_board(width, height)
    board4 = engine.create_board(width, height)
    board2[3][1] = "O"
    board2[19][3] = '&'
    engine.put_helmet2_on_board(board2,steel_helmet)
    engine.create_potion(board3)
    engine.create_potion2(board3)
    walls.board1_walls(board)
    walls.board2_walls(board2)
    walls.board3_walls(board3)
    walls.board4_boss(board4)
    mobs.put_cpu1_on_board(board,cpu_1)
    mobs.put_cpu2_on_board(board,cpu_2)
    mobs.put_cpu3_on_board(board,cpu_3)
    mobs.put_cpu4_on_board(board,cpu_4)


    using_map = board

    items = ['/','*','$','<','>','^','m','M', 'O',' ','=','g','G',']','&','!','?',')','B']
    board3[9][6] = "="
    board3[7][9] = "O"
    board3[5][18] = '&'
    engine.put_bread_on_board(board, bread)
    engine.put_helmet_on_board(board, wooden_helmet)
    engine.put_sword_on_board(board, wooden_sword)
    engine.put_sword_on_board(board2, steel_sword)
    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(using_map, player)
        ui.display_board(using_map,player,inventory)
        engine.remove_player_from_board(using_map, player)

        key = util.key_pressed()
        field = engine.player_movement(key, using_map, player,items,inventory)
        if field in items:
            engine.add_to_inventory(inventory, field, player)
        if using_map == board3 and field == ' ' and player["x"] == 23 and player["y"] == 1 and "enchanted_helmet" not in inventory:
            field = '^'
            engine.add_to_inventory(inventory,field,player)
            print("----YOU FOUND AN ARTEFACT!")
            sleep(2)
        if using_map == board2 and field == ' ' and player["x"] == 2 and player["y"] == 23 and "magic_sword" not in inventory:
            field = ']'
            engine.add_to_inventory(inventory,field,player)
            print("----YOU FOUND AN ARTEFACT!")
            sleep(2)
        if field == "=":
            if "Key" not in inventory:
                player["player_health"] = 0
                engine.player_death(player)
        if field == 'm':
            print("---------------BATTLE BEGINS-------------------")
            while cpu_1['cpu_health'] > 0:
                engine.fight_with_NPC(cpu_1, player)
                engine.player_death(player)
            else:
                print('-----------------YOU WIN-------------')
                sleep(2)
        elif field == 'M':
            print("---------------BATTLE BEGINS-------------------")
            while cpu_4['cpu_health'] > 0:
                engine.fight_with_NPC(cpu_4, player)
                engine.player_death(player)         
            else:
                print('-----------------YOU WIN-------------')
                sleep(2)
                using_map[1][1] = 'O'
        elif field == 'g':
            print("---------------BATTLE BEGINS-------------------")
            while cpu_2['cpu_health'] > 0:
                engine.fight_with_NPC(cpu_2, player)
                engine.player_death(player)
            else:
                print('-----------------YOU WIN-------------')
                sleep(2) 
        elif field == "B":
            print("---------------BATTLE BEGINS-------------------")
            while boss['cpu_health'] > 0:
                engine.fight_with_NPC(boss,player)
                engine.player_death(player)
            else:
                walls.clear_and_win()
                
        elif field == 'G':
            print("---------------BATTLE BEGINS-------------------")
            while cpu_3['cpu_health'] > 0:
                engine.fight_with_NPC(cpu_3, player)
                engine.player_death(player)
            else:
                print('-----------------YOU WIN-------------')
                sleep(2)
                inventory.append("Key")
                print("=========Monster Dropped Key=========")
                sleep(2)
        if field == 'O':
            player["x"] = 1
            player["y"] = 1
            
            if using_map == board:
                using_map = board2
                engine.bread_change_place(bread)
                engine.put_bread_on_board(board2,bread)
            elif using_map == board2:
                using_map = board3
                mobs.enemy1_change_position(cpu_1)
                mobs.enemy2_change_position(cpu_2)
                mobs.enemy3_change_position(cpu_3)
                mobs.put_cpu1_on_board(using_map,cpu_1)
                mobs.put_cpu2_on_board(using_map,cpu_2)
                mobs.put_cpu3_on_board(using_map,cpu_3)
                
                engine.bread_change2_place(bread)
                engine.put_bread_on_board(using_map,bread)
            elif using_map == board3:
                using_map = board4
                if "magic_sword" in inventory and "enchanted_helmet" in inventory:
                    print(" -----SOME KIND OF MYSTERIOUS POWER SURROUNDS YOU ")
                    sleep(2)
                    print(" ----YOU ARE GETTING STRONGER")
                    sleep(2)
                    player["player_health"] = 200
                engine.bread_change_place(bread)
                engine.put_bread_on_board(using_map,bread)
        util.clear_screen()

if __name__ == '__main__':
    main()
