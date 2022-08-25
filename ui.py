def display_board(board,player,inventory:list):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    for element in board:
        print(*element)
    
    print("Small Legend:\n Move : 'WASD'\n small letters = small monsters\n BIG LETTERS = BIG MONSTERS\n Press L: Bigger Legend\n Press I: Equipment\n Press Q: Show Quest")