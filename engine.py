from time import sleep
import random

def create_board(width, height):
    board = [[' ' for x in range(height)] for y in range(width)]
    for i in range(len(board)):
        board[i][height-1] = '#' 
        board[width-1][i] = '#'
        board[i][0] = '#'
        board[0][i] = '#'    

    return board

def create_vertical_wall(board, x_start, y, x_end):
    '''
    x = width of map
    y = height of map
    '''
    while x_end != x_start:
        board[x_start][y] = '#'
        x_start += 1 

def create_horizontal_wall(board, y_start, x, y_end):
    while y_end != y_start:
        board[x][y_start] = '#'
        y_start += 1 

def put_player_on_board(board, player):
    board[player["y"]][player["x"]] = player["player_icon"]
    return board

def remove_player_from_board(board, player):
    board[player['y']][player['x']] = ' '

def player_death(player):
    if player['player_health'] <= 0:
        print('You have died!')
        sleep(5)
        exit()

def player_movement(key, board, player,items):
    
    
    if key == 'q':
        exit()
    if key == 'i':
        print('Opened inventory')
    elif key == 'w':
        if board[player['y']-1][player['x']] != '#':
            player['y'] -= 1
            if board[player['y']][player['x']] in items:
                return board[player['y']][player['x']]                
    elif key == 's':
        if board[player['y']+1][player['x']] != '#':
            player['y'] += 1
            if board[player['y']][player['x']] in items:
                return board[player['y']][player['x']]
    elif key == 'a':
        if board[player['y']][player['x']-1] != '#':
            player['x'] -= 1
            if board[player['y']][player['x']] in items:
                return board[player['y']][player['x']]
    elif key == 'd':
        if board[player['y']][player['x']+1] != '#':
            player['x'] += 1
            if board[player['y']][player['x']] in items:
                return board[player['y']][player['x']]

def add_to_inventory(inventory, field, player):
    if field == "*":
        player['player_health'] += 4
    elif field == "<":
        inventory_exchange(player,inventory,item_value,"wooden_helmet")
    elif field == ">":
        inventory_exchange(player,inventory,item_value,"steel_helmet")
    elif field == "^":
        inventory_exchange(player,inventory,item_value,"enchanted_helmet")
    elif field == "/":
        inventory_exchange(player,inventory,item_value,"wooden_sword")
    elif field == "$":
        inventory.append("Key")
    return inventory, player

def create_enemy_map1(position_list):
    enemy_x_place = [2,3,4,5,6,7,8]
    enemy_y_place = [2,3,4,5,6,7,8]

    cpu_1 = {
        "cpu_icon" : "m",
        "x" : random.choice(enemy_x_place),
        "y" : random.choice(enemy_y_place),
        "cpu_health" : 8,
        "attack_power": 7,
        "defence": 0}
    check_position(position_list,cpu_1)
    position_list.append((cpu_1["y"],cpu_1["x"]))
    return cpu_1

def create_enemy_map2(position_list):
    enemy_x_place = [2,3,4,5,6,7,8]
    enemy_y_place = [2,3,4,5,6,7,8]

    cpu_1 = {
        "cpu_icon" : "m",
        "x" : random.choice(enemy_x_place),
        "y" : random.choice(enemy_y_place),
        "cpu_health" : 8,
        "attack_power": 7,
        "defence": 0}
    check_position(position_list,cpu_1)
    position_list.append((cpu_1["y"],cpu_1["x"]))
    return cpu_1

def create_enemy_2_map1(position_list):
    enemy2_x_place = [2,3,4,5,6,7,8]
    enemy2_y_place = [2,3,4,5,6,7,8]

    cpu_2 = {
        "cpu2_icon" : "M",
        "x" : random.choice(enemy2_x_place),
        "y" : random.choice(enemy2_y_place),
        "cpu_health" : 10,
        "attack_power": 8,
        "defence": 1}
    check_position(position_list,cpu_2)
    position_list.append((cpu_2["y"],cpu_2["x"]))
    return cpu_2

def put_cpu1_on_board(board, cpu_1):
    board[cpu_1["y"]][cpu_1["x"]] = cpu_1["cpu_icon"]
    return board

def put_cpu2_on_board(board, cpu_2):
    board[cpu_2["y"]][cpu_2["x"]] = cpu_2["cpu2_icon"]
    return board

def create_bread(position_list):
    x_place = [2,3,4,5,6,7,8]
    y_place = [2,3,4,5,6,7,8]

    bread = {
        "bread_icon" : "*",
        "x" : random.choice(x_place),
        "y" : random.choice(y_place),
        "health": 5}
    check_position(position_list,bread)
    position_list.append((bread["y"],bread["x"]))
    return bread

def put_bread_on_board(board, object):
    board[object["y"]][object["x"]] = object["bread_icon"]
    return board

def create_wooden_helmet(position_list):
    x_place = [2,3,4,5,6,7,8]
    y_place = [2,3,4,5,6,7,8]

    wooden_helmet = {
        "wooden_helmet_icon" : "<",
        "x" : random.choice(x_place),
        "y" : random.choice(y_place),}
    check_position(position_list,wooden_helmet)
    position_list.append((wooden_helmet["y"],wooden_helmet["x"]))
    return wooden_helmet

def create_steel_helmet(position_list):
    x_place = [2,3,4,5,6,7,8]
    y_place = [2,3,4,5,6,7,8]

    steel_helmet = {
        "steel_helmet_icon" : ">",
        "x" : random.choice(x_place),
        "y" : random.choice(y_place)}
    check_position(position_list,steel_helmet)
    position_list.append((steel_helmet["y"],steel_helmet["x"]))
    return steel_helmet

def create_enchanted_helmet(position_list):
    x_place = [2,3,4,5,6,7,8]
    y_place = [2,3,4,5,6,7,8]

    enchanted_helmet = {
        "enchanted_helmet_icon" : "^",
        "x" : random.choice(x_place),
        "y" : random.choice(y_place)}
    check_position(position_list,enchanted_helmet)
    position_list.append((enchanted_helmet["y"],enchanted_helmet["x"]))
    return enchanted_helmet


def put_helmet_on_board(board, object):
    board[object["y"]][object["x"]] = object["wooden_helmet_icon"]
    return board
def put_helmet2_on_board(board, object):
    board[object["y"]][object["x"]] = object["steel_helmet_icon"]
    return board
def put_helmet3_on_board(board, object):
    board[object["y"]][object["x"]] = object["enchanted_helmet_icon"]
    return board

def create_sword(position_list):
    x_place = [2,3,4,5,6,7,8]
    y_place = [2,3,4,5,6,7,8]

    sword = {
        "sword_icon" : "/",
        "x" : random.choice(x_place),
        "y" : random.choice(y_place),
        "attack_add": 5}
    check_position(position_list,sword)
    position_list.append((sword["y"],sword["x"]))
    return sword

def put_sword_on_board(board, object):
    board[object["y"]][object["x"]] = object["sword_icon"]
    return board

def check_position(position_list, object):
    coordinates = [2,3,4,5,6,7,8]
    while True:
        if (object["y"],object["x"]) in position_list:
            object["y"] = random.choice(coordinates)
            object["x"] = random.choice(coordinates)
        else:
            return True

def fight_with_NPC(NPC: str, player:str):
    if player['player_attack'] - NPC['defence'] >0:
        NPC['cpu_health'] = NPC['cpu_health'] - (player['player_attack'] - NPC['defence'])
    if (NPC['attack_power'] - player['player_defense']) >= 0:
        player['player_health'] = player['player_health'] - (NPC['attack_power'] - player['player_defense'])


def inventory_value():
    item_value = {
        "wooden_sword" : 2,
        "steel_sword" : 4,
        "bow" : 5,
        "wooden_helmet" : 2,
        "steel_helmet" : 4,
        "enchanted_helmet" : 6,
        "wooden_armor" : 2,
        "steel_armor" : 4,
        "diamond_armor" : 6,
        "shield" : 4,
        "Magic Scroll" : 2,
        "Water Magic Scroll" : 4,
        "Fire Magic Scroll" : 6,
        "heal_potion" : 5,
        "strength_potion" : 5,
        "power_potion" : 5,
        }
    return item_value
item_value = inventory_value()
sword_items = ["wooden_sword","steel_sword","bow"]
helmet_items = ["wooden_helmet","steel_helmet","enchanted_helmet"]
armor_items = ["wooden_armor","steel_armor","diamond_armor"]
shield_items = ["shield"]
scroll_items = ["Magic Scroll","Water Magic Scroll","Fire Magic Scroll"]
potion_items = ["heal_potion","strength_potion","power_potion","death_potion"]


def inventory_exchange(player,inventory:list,item_value,item):
    if item in sword_items:
        if player["equipped_sword"] == "":
            print(item_value[item])
            player["equipped_sword"] = item
            player["player_attack"] += item_value[item]
            inventory.append(item)
            return player
        else:
            player["player_attack"] -= item_value[player["equipped_sword"]]
            player["player_attack"] += item_value[item]
            player["equipped_sword"] = item
            inventory.append(item)
            return player
    elif item in helmet_items:
        if player["equipped_helmet"] == "":
            print(item_value[item])
            print(item)
            player["equipped_helmet"] = item
            player["player_defense"] += item_value[item]
            inventory.append(item)
            return player
        else:
            player["player_defense"] -= item_value[player["equipped_helmet"]]
            player["player_defense"] += item_value[item]
            player["equipped_helmet"] = item
            inventory.append(item)
            return player
    elif item in armor_items:
        if player["equipped_armor"] == "":
            player["equipped_armor"] = item
            player["player_defense"] += item_value[item]
            inventory.append(item)
            return player
        else:
            player["player_defense"] -= item_value[player["equipped_armor"]]
            player["player_defense"] += item_value[item]
            player["equipped_armor"] = item
            inventory.append(item)
            return player
    elif item in shield_items:
        if player["equipped_shield"] == "":
            player["equipped_shield"] = item
            player["player_defense"] += item_value[item]
            inventory.append(item)
            return player
        else:
            player["player_defense"] -= item_value[player["equipped_shield"]]
            player["player_defense"] += item_value[item]
            player["equipped_shield"] = item
            inventory.append(item)
            return player
    elif item in scroll_items:
        if player["equipped_weapon2"] == "":
            player["equipped_weapon2"] = item
            player["player_attack"] += item_value[item]
            inventory.append(item)
            return player
        else:
            player["player_attack"] -= item_value[player["equipped_weapon2"]]
            player["player_attack"] += item_value[item]
            player["equipped_weapon2"] = item
            inventory.append(item)
            return player
    elif item in potion_items:
        if item == "heal_potion":
            player["player_health"] += 10
            return player
        elif item == "strength_potion":
            player["player_health"] += 2
            player["player_attack"] += 5
            player["player_defense"] += 5
            return player
        elif item == "power_potion":
            player["player_health"] += 8
            player["player_attack"] += 2
            player["player_defense"] += 2
            return player
        elif item == "death_potion":
            player["player_health"] = 0
            return player