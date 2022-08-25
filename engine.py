from time import sleep
import random
import time

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

def player_movement(key, board, player,items,inventory):
    
    
    if key == 'q':
        print("Quest:\n- YOU HAVE TO FIND MAGIC EQUIPMENT TO DEFEAT THE SCARY MONSTER!")
        sleep(3)
    if key == 't':
        cheats = input("Podaj Cheata: ")
        if cheats == "portal":
            board[1][1] = "O"
        if cheats == "quest":
            player["player_health"] = 200
            player['player_attack'] += 200
            player['player_defense'] += 200
        sleep(2)
    if key == 'l':
        print("The Full Legend:\n O - PORTAL DO NEXT LVL\n / - drewniany miecz\n ) - stalowy miecz\n & - wskazówka\n < - drewniany hełm\n > - stalowy hełm\n = - Kolczatka/drzwi\n ! - mikstura życia\n ? - tajemnicza mikstura\n Magiczny miecz = Nieznane | Zaklęty hełm = nieznane")
        sleep(6)
    if key == 'i':
        print('Opened inventory')
        for i in inventory:
            print("-",i)
        sleep(4)
    if key == 'p':
        print(f"\nStatistics:\nHealth : {player['player_health']} \nPlayer Attack : {player['player_attack']}\nPlayer_defense : {player['player_defense']}")
        sleep(4)
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
    elif field == ")":
        inventory_exchange(player,inventory,item_value,"steel_sword") 
    elif field == "]":
        inventory_exchange(player,inventory,item_value,"magic_sword")
    elif field == "$":
        inventory.append("Key")
    elif field == "?":
        inventory_exchange(player,inventory,item_value,"death_potion")
    elif field == "!":
        inventory_exchange(player,inventory,item_value,"power_potion")
    elif field == '&':
        print("----------------------------THE ARTEFACT IS CLOSE------------------------")
        sleep(2)
    return inventory, player




def create_potion(board):
    board[22][3] = "?"
    return board
def create_potion2(board):
    board[21][4] = "!"
    return board

def potion_placing(board):
    create_potion(board)
    create_potion2(board)
    return board

def create_bread(position_list):
    bread = {
        "bread_icon" : "*",
        "x" : 7,
        "y" : 23,}
    check_position(position_list,bread)
    position_list.append((bread["y"],bread["x"]))
    return bread
def bread_change_place(bread):
    bread["x"] = 15
    bread["y"] = 14
    return bread
def bread_change2_place(bread):
    bread["x"] = 22
    bread["y"] = 21
    return bread

def put_bread_on_board(board, object):
    board[object["y"]][object["x"]] = object["bread_icon"]
    return board

def create_wooden_helmet(position_list):
    wooden_helmet = {
        "wooden_helmet_icon" : "<",
        "x" : 16,
        "y" : 9,}
    check_position(position_list,wooden_helmet)
    position_list.append((wooden_helmet["y"],wooden_helmet["x"]))
    return wooden_helmet

def create_steel_helmet(position_list):
    steel_helmet = {
        "steel_helmet_icon" : ">",
        "x" : 18,
        "y" : 18}
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
    sword = {
        "sword_icon" : "/",
        "x" : 23,
        "y" : 2,
        "attack_add": 5}
    check_position(position_list,sword)
    position_list.append((sword["y"],sword["x"]))
    return sword

def create_sword2(position_list):
    steel_sword = {
        "sword_icon" : ")",
        "x" : 20,
        "y" : 2,
        "attack_add": 5}
    check_position(position_list,steel_sword)
    position_list.append((steel_sword["y"],steel_sword["x"]))
    return steel_sword

def put_sword_on_board(board, object):
    board[object["y"]][object["x"]] = object["sword_icon"]
    return board

def check_position(position_list, object):
    coordinates = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    while True:
        if (object["y"],object["x"]) in position_list:
            object["y"] = random.choice(coordinates)
            object["x"] = random.choice(coordinates)
        else:
            return True

def fight_with_NPC(NPC, player):
    dealed_dmg = ()
    gained_dmg = ()
    if player['player_attack'] - NPC['defence'] >0:
        NPC['cpu_health'] = NPC['cpu_health'] - (player['player_attack'] - NPC['defence'])
        dealed_dmg = player['player_attack'] - NPC['defence']
        print(f" YOU DEALED: {dealed_dmg} DAMEGE")
        sleep(1)
    if (NPC['attack_power'] - player['player_defense']) >= 0:
        player['player_health'] = player['player_health'] - (NPC['attack_power'] - player['player_defense'])
        gained_dmg = NPC['attack_power'] - player['player_defense']
        print(f" YOU GAINED: {gained_dmg} DAMAGE")
        sleep(1)

def inventory_value():
    item_value = {
        "wooden_sword" : 2,
        "steel_sword" : 5,
        "magic_sword" : 180,
        "wooden_helmet" : 2,
        "steel_helmet" : 6,
        "enchanted_helmet" : 100,
        "wooden_armor" : 2,
        "steel_armor" : 4,
        "diamond_armor" : 6,
        "shield" : 4,
        "Magic Scroll" : 3,
        "Water Magic Scroll" : 6,
        "Fire Magic Scroll" : 9,
        "heal_potion" : 10,
        "strength_potion" : 20,
        "power_potion" : 30,
        }
    return item_value
item_value = inventory_value()
sword_items = ["wooden_sword","steel_sword","bow","magic_sword"]
helmet_items = ["wooden_helmet","steel_helmet","enchanted_helmet"]
armor_items = ["wooden_armor","steel_armor","diamond_armor"]
shield_items = ["shield"]
scroll_items = ["Magic Scroll","Water Magic Scroll","Fire Magic Scroll"]
potion_items = ["heal_potion","strength_potion","power_potion","death_potion"]


def inventory_exchange(player,inventory:list,item_value,item):
    if item in sword_items:
        if player["equipped_sword"] == "":
            player["equipped_sword"] = item
            player["player_attack"] += item_value[item]
            if item not in inventory:
                inventory.append(item)
            return player
        else:
            player["player_attack"] -= item_value[player["equipped_sword"]]
            inventory.remove(player["equipped_sword"])
            player["player_attack"] += item_value[item]
            player["equipped_sword"] = item
            if item not in inventory:
                inventory.append(item)
            return player
    elif item in helmet_items:
        if player["equipped_helmet"] == "":
            print(item_value[item])
            print(item)
            player["equipped_helmet"] = item
            player["player_defense"] += item_value[item]
            if item not in inventory:
                inventory.append(item)
            return player
        else:
            player["player_defense"] -= item_value[player["equipped_helmet"]]
            inventory.remove(player["equipped_helmet"])
            player["player_defense"] += item_value[item]
            player["equipped_helmet"] = item
            if item not in inventory:
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
            player["player_health"] += 20
            player["player_attack"] += 5
            player["player_defense"] += 5
            return player
        elif item == "power_potion":
            player["player_health"] += 30
            player["player_attack"] += 10
            player["player_defense"] += 20
            return player
        elif item == "death_potion":
            player["player_health"] = 0
            player_death(player)
            return player