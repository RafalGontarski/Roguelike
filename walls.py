import engine
import ui
import util


def board3_walls(board):
    engine.create_vertical_wall(board,1,2,10)
    engine.create_vertical_wall(board,1,3,10)
    engine.create_vertical_wall(board,1,4,10)
    engine.create_vertical_wall(board,1,5,10)
    engine.create_vertical_wall(board,1,13,10)
    engine.create_vertical_wall(board,12,13,24)
    engine.create_horizontal_wall(board,7,9,14)
    engine.create_horizontal_wall(board,15,9,24)
    engine.create_horizontal_wall(board,15,11,23)
    engine.create_horizontal_wall(board,15,12,23)
    engine.create_horizontal_wall(board,15,13,23)
    engine.create_horizontal_wall(board,15,14,23)
    engine.create_horizontal_wall(board,15,15,23)
    engine.create_horizontal_wall(board,15,16,23)
    engine.create_horizontal_wall(board,15,17,23)
    engine.create_horizontal_wall(board,14,19,23)
    engine.create_horizontal_wall(board,14,20,16)
    engine.create_horizontal_wall(board,15,22,16)
    engine.create_horizontal_wall(board,15,23,16)
    engine.create_horizontal_wall(board,1,11,12)
    engine.create_horizontal_wall(board,13,11,14)
    engine.create_horizontal_wall(board,7,8,14)
    engine.create_horizontal_wall(board,2,13,14)
    engine.create_horizontal_wall(board,1,15,12)
    engine.create_horizontal_wall(board,2,17,14)
    engine.create_horizontal_wall(board,1,19,12)
    return board


