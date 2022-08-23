def display_board(board,player,inventory):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    for element in board:
        print(*element)

    print(f"\nInventory: {inventory}")
    print(f"\nStatistics:\nHealth : {player['player_health']} \nPlayer Attack : {player['player_attack']}\nPlayer_defense : {player['player_defense']}")