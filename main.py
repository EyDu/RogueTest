import engine
import ui
import movement
import os
import keyboard
import time

# Start Setup

player_x = 4
player_y = 2
current_level = 1


if __name__ == '__main__':
    while True:
        user_input = False
        old_player_x = player_x
        old_player_y = player_y
        os.system('clear')
        board = engine.create_board(current_level)
        ui.display_board(engine.put_player_on_board(player_x, player_y, board))
        player_x, player_y = movement.move_player_and_wall_block(old_player_x, old_player_y, board)
        player_x, current_level = movement.next_level(player_x, player_y, board, current_level)
        time.sleep(0.2)
        