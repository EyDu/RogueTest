import engine

WHITE = '\x1b[0;39;47m'
GREEN = '\x1b[0;39;42m'
RED = '\x1b[0;39;41m'
BROWN = '\x1b[0;39;43m'
YELLOW = '\x1b[0;39;45m'


COLOR_END = '\x1b[0m'

def display_board(board):
    for array in board:
        counter = 0
        for elem in array:
            counter += 1
            #Paint The Walls
            if elem == 1 and counter == len(array):
                print(WHITE + ' ' + COLOR_END)
            elif elem == 1:
                print(WHITE + ' ' + COLOR_END, end='')
            elif elem == 0:
                print(GREEN + ' ' + COLOR_END, end='')
            #Paint the door
            elif elem == 2 and counter == len(array):
                print(BROWN + ' ' + COLOR_END)
            elif elem == 2:
                print(BROWN + ' ' + COLOR_END, end='')
            #paint the player
            elif elem == 3:
                print(YELLOW + 'P' + COLOR_END, end='')
            #paint the enemies
            elif elem == 4:
                print(RED + 'O' + COLOR_END, end='')
            elif elem == 5:
                print(RED + 'A' + COLOR_END, end='')
            elif elem == 6:
                print(RED + 'W' + COLOR_END, end='')
            #paint the boss
            elif elem == 8:
                print(RED + 'B' + COLOR_END, end='')
            elif elem == 9:
                print(RED + ' ' + COLOR_END, end='')
            
            else:
                print(elem, end='')
            

                
display_board(engine.put_player_on_board(3, 5, engine.create_board(1)))

