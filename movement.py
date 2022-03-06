import keyboard


def move_player(old_player_x, old_player_y):
    if keyboard.w:
        player_y = old_player_y - 1
        return old_player_x, player_y
    elif keyboard.a:
        player_x = old_player_x - 1
        return player_x, old_player_y
    elif keyboard.s:
        player_y = old_player_y + 1
        return old_player_x, player_y
    elif keyboard.d:
        player_x = old_player_x + 1
        return player_x, old_player_y

def wall_block(player_x, player_y, old_player_x, old_player_y, board):
    if board[player_y][old_player_x] == 1 or board[old_player_x][player_y] == 1:
        player_x = old_player_x
        player_y = old_player_y
    return player_x, player_y
    
def next_level(player_x, player_y, board, current_level):
    if board[player_y][player_x] == 2 and player_y != 0:
        current_level += 1
    elif board[player_y][player_x] == 2 and player_y == 0:
        current_level -= 1
    return current_level