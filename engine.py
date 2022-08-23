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
    if key == 'q':
        exit()
    if key == 'i':
        print('Opened inventory')
    elif key == 'w':
        if board[player['y']-1][player['x']] != '#':
            player['y'] -= 1
    elif key == 's':
        if board[player['y']+1][player['x']] != '#':
            player['y'] += 1
    elif key == 'a':
        if board[player['y']][player['x']-1] != '#':
            player['x'] -= 1
    elif key == 'd':
        if board[player['y']][player['x']+1] != '#':
            player['x'] += 1