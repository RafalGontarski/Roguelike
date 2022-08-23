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

def put_player_on_board(board, player):
    board[player["y"]][player["x"]] = player["player_icon"]
    return board

def remove_player_from_board(board, player):
    board[player['y']][player['x']] = ' '

def player_movement(key, board, player):
    fields = ['*', '/', '^', '$']
    
    if key == 'q':
        exit()
    if key == 'i':
        print('Opened inventory')
    elif key == 'w':
        if board[player['y']-1][player['x']] != '#':
            player['y'] -= 1
            if board[player['y']][player['x']] in fields:
                return board[player['y']][player['x']]                
    elif key == 's':
        if board[player['y']+1][player['x']] != '#':
            player['y'] += 1
            if board[player['y']][player['x']] in fields:
                return board[player['y']][player['x']]
    elif key == 'a':
        if board[player['y']][player['x']-1] != '#':
            player['x'] -= 1
            if board[player['y']][player['x']] in fields:
                return board[player['y']][player['x']]
    elif key == 'd':
        if board[player['y']][player['x']+1] != '#':
            player['x'] += 1
            if board[player['y']][player['x']] in fields:
                return board[player['y']][player['x']]

def add_to_inventory(inventory, field, player):
    if field == "*":
        player['player_health'] += 10
    elif field == "^":
        inventory.append("Helmet")
        player['player_defense'] += 10
    elif field == "/":
        inventory.append("Sword")
        player['player_attack'] += 10
    elif field == "$":
        inventory.append("Key")
    return inventory, player

def create_enemy(position_list):
    enemy_x_place = [2,3,4,5,6,7,8]
    enemy_y_place = [2,3,4,5,6,7,8]

    cpu_1 = {
        "cpu_icon" : "m",
        "x" : random.choice(enemy_x_place),
        "y" : random.choice(enemy_y_place),
        "cpu_health" : 5,
        "attack_power": 1,
        "defence": 0}
    check_position(position_list,cpu_1)
    position_list.append((cpu_1["y"],cpu_1["x"]))
    return cpu_1

def create_enemy_2(position_list):
    enemy2_x_place = [2,3,4,5,6,7,8]
    enemy2_y_place = [2,3,4,5,6,7,8]

    cpu_2 = {
        "cpu2_icon" : "M",
        "x" : random.choice(enemy2_x_place),
        "y" : random.choice(enemy2_y_place),
        "cpu2_health" : 10,
        "attack_power": 2,
        "defence": 2}
    check_position(position_list,cpu_2)
    position_list.append((cpu_2["y"],cpu_2["x"]))
    return cpu_2

def put_cpu2_on_board(board, cpu_2):
    board[cpu_2["y"]][cpu_2["x"]] = cpu_2["cpu2_icon"]
    return board

def put_cpu1_on_board(board, cpu_1):
    board[cpu_1["y"]][cpu_1["x"]] = cpu_1["cpu_icon"]
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

def create_helmet(position_list):
    x_place = [2,3,4,5,6,7,8]
    y_place = [2,3,4,5,6,7,8]

    helmet = {
        "helmet_icon" : "^",
        "x" : random.choice(x_place),
        "y" : random.choice(y_place),
        "defence_add": 5}
    check_position(position_list,helmet)
    position_list.append((helmet["y"],helmet["x"]))
    return helmet

def put_helmet_on_board(board, object):
    board[object["y"]][object["x"]] = object["helmet_icon"]
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
