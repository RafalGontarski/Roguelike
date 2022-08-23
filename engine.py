from time import sleep

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
        player['player health'] += 1
    elif field == "^":
        inventory.append("Helmet")
    elif field == "/":
        inventory.append("Sword")
    elif field == "$":
        inventory.append("Key")
    return inventory, player