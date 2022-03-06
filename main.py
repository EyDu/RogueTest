from syslog import LOG_LOCAL0
import engine
import ui
import movement
import os

# Start Setup

player_x = 2
player_y = 2
current_level = 1


if __name__ == '__main__':
    while True:
        os.system('clear')
        ui.display_board(engine.put_player_on_board(player_x, player_y, engine.create_board(current_level)))
        
        LOG_LOCAL0