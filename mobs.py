import engine
import random
def create_enemy_map1(position_list):
    cpu_1 = {
        "cpu1_icon" : "m",
        "x" : 1,
        "y" : 9,
        "cpu_health" : 8,
        "max_health" : 8,
        "attack_power": 5,
        "defence": 0}
    engine.check_position(position_list,cpu_1)
    position_list.append((cpu_1["y"],cpu_1["x"]))
    return cpu_1

def put_cpu1_on_board(board, cpu_1):
    board[cpu_1["y"]][cpu_1["x"]] = cpu_1["cpu1_icon"]
    return board

def create_enemy2_map1(position_list):
    cpu_2 = {
        "cpu2_icon" : "g",
        "x" : 1,
        "y" : 22,
        "cpu_health" : 5,
        "max_health" : 5,
        "attack_power":5,
        "defence": 0}
    engine.check_position(position_list,cpu_2)
    position_list.append((cpu_2["y"],cpu_2["x"]))
    return cpu_2

def put_cpu2_on_board(board, cpu_2):
    board[cpu_2["y"]][cpu_2["x"]] = cpu_2["cpu2_icon"]
    return board

def create_enemy3_map1(position_list):
    cpu_3 = {
        "cpu3_icon" : "G",
        "x" : 1,
        "y" : 22,
        "cpu_health" : 8,
        "max_health" : 12,
        "attack_power": 10,
        "defence": 2}
    engine.check_position(position_list,cpu_3)
    position_list.append((cpu_3["y"],cpu_3["x"]))
    return cpu_3

def put_cpu3_on_board(board, cpu_3):
    board[cpu_3["y"]][cpu_3["x"]] = cpu_3["cpu3_icon"]
    return board

def create_enemy4_map1(position_list):
    cpu_4 = {
        "cpu4_icon" : "M",
        "x" : 23,
        "y" : 23,
        "cpu_health" : 12,
        "max_health" : 16,
        "attack_power": 8,
        "defence": 4}
    engine.check_position(position_list,cpu_4)
    position_list.append((cpu_4["y"],cpu_4["x"]))
    return cpu_4

def put_cpu4_on_board(board, cpu_4):
    board[cpu_4["y"]][cpu_4["x"]] = cpu_4["cpu4_icon"]
    return board

def mob_max_hp(cpu):
    cpu["cpu_health"] = cpu["max_health"]
    return cpu

def create_boss(position_list):
    
    size_boss = 5
    boss_x_place = [2,3,4,5,6,7,8]
    boss_y_place = [2,3,4,5,6,7,8]

    boss = {
        "boss_icon" : 'B',
        "x" : random.choice(boss_x_place),
        "y" : random.choice(boss_y_place),
        "boss_health" : 8,
        "attack_power": 7,
        "defence": 0
        }
    
    size_boss = 5

    for c in range(size_boss):
        for r in range(size_boss):
            print(boss['boss_icon'], end='')    
        print()
        
    
    
    check_position(position_list,boss)
    position_list.append((boss["y"],boss["x"]))
    
    return boss

def put_boss_on_board(board, boss):
    board[boss["y"]][boss["x"]] = boss["boss_icon"]
    return board

def boss_movement(board, boss):
    xy = ['x', 'y']
    random_xy = random.choice(xy)
    sides = (+1, -1)
    random_sides = random.choice(sides)
    player_key = util.key_pressed()
    if player_key:
        boss[random_xy] = boss[random_xy] + random_sides
    if player_key and board[boss['y'] - 1][boss['x']] != '#':
        boss['y'] -=1
    if player_key and board[boss['y'] + 1][boss['x']] != '#':
        boss['y'] +=1
    if player_key and board[boss['y']][boss['x'] - 1] != '#':
        boss['x'] -=1
    if player_key and board[boss['y']][boss['x'] + 1] != '#':
        boss['x'] +=1