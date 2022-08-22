def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    board = [[' ' for x in range(height)] for y in range(width)]
    for i in range(len(board)):
        board[i][height-1] = '#' 
        board[width-1][i] = '#'
        board[i][0] = '#'
        board[0][i] = '#'    
    return board



def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass