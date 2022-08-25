def display_board(board,player,inventory:list):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    for element in board:
        print(*element)
    health = player["player_health"]
    print(f"Small Legend:         Health:{health}\n Move : 'WASD'\n small letters = small monsters\n BIG LETTERS = BIG MONSTERS\n Press P: Stats\n Press L: Bigger Legend\n Press I: Equipment\n Press Q: Show Quest")