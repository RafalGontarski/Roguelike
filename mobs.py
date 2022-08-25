import engine


def place_mobs_round1(board,cpu_1,cpu_2,):
    engine.put_cpu1_on_board(board,cpu_1)
    engine.put_cpu2_on_board(board, cpu_2)
    return board

def place_mobs_round2(board,cpu_3,cpu_4):
    engine.put_cpu1_on_board(board,cpu_3)
    engine.put_cpu2_on_board(board, cpu_4)
    return board
    