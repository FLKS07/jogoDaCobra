import terminal
import random

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


apple_position_x = 0
apple_position_y = 0

def generate_apple(caudas, x, y):
    global apple_position_x
    global apple_position_y

    apple_position_y = random.randrange(2,terminal.console_height)
    apple_position_x = random.randrange(1,terminal.console_width)

    
    
    while(checkPos(caudas,x,y)):
        apple_position_y = random.randrange(2,terminal.console_height)
        apple_position_x = random.randrange(1,terminal.console_width)

    print_apple()

    
def clear_apple():
    global apple_position_y
    global apple_position_x
    terminal.print_at(apple_position_x, apple_position_y, ' ')

        

def checkPos(caudas, x, y):
    for segment in caudas:
        if segment.x == apple_position_x and segment.y == apple_position_y:
            return True
        if x == apple_position_x and y == apple_position_y:
            return True
        return False
    

def print_apple():
    
    terminal.print_at(apple_position_x, apple_position_y, f"{Fore.RED}H{Style.RESET_ALL}")
    