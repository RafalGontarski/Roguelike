def display_board(board, player):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    for element in board:
        print(*element)
    print(f"\nPlayer health is: {player['player_health']}")