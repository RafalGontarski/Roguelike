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