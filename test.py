import keyboard
import os


def something():
    while True:
        if keyboard.is_pressed('w'):
            os.system('clear')
            print("nice!")
            break             
something()