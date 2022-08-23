def display_board(board,player,inventory:list):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    for element in board:
        print(*element)
    inv_to_print = ''
    for element in inventory:
        inv_to_print += element + ', '
    print(f"\nStatistics:\nHealth : {player['player_health']} \nPlayer Attack : {player['player_attack']}\nPlayer_defense : {player['player_defense']}")
    print(f"\nInventory: {inv_to_print}")