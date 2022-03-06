import keyboard


def move_player_and_wall_block(old_player_x, old_player_y, board):
    while True:
        if keyboard.is_pressed('w'):
            player_x = old_player_x
            player_y = old_player_y - 1 
            break
        elif keyboard.is_pressed('a'):
            player_x = old_player_x - 1
            player_y = old_player_y
            break
        elif keyboard.is_pressed('s'):
            player_x = old_player_x
            player_y = old_player_y + 1
            break
        elif keyboard.is_pressed('d'):
            player_x = old_player_x + 1
            player_y = old_player_y
            break
    if wall_block(player_x, player_y, board):
        return old_player_x, old_player_y
    else:
        return player_x, player_y

def wall_block(player_x, player_y, board):
    if board[player_y][player_x] == 1:
        print('BLOCKED')
        return True
    else:
        return False

  
def next_level(player_x, player_y, board, current_level):
    if board[player_y][player_x] == 2 and player_x != 0:
        current_level += 1
        player_x = 1
    elif board[player_y][player_x] == 2 and player_x == 0:
        player_x = len(board)
        current_level -= 1
    return player_x, current_level

