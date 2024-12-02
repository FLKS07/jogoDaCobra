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

    apple_position_y = random.randrange(1,terminal.console_height)
    apple_position_x = random.randrange(1,terminal.console_width)

    
    
    while(checkPos(caudas,x,y)):
        apple_position_y = random.randrange(1,terminal.console_height)
        apple_position_x = random.randrange(1,terminal.console_width)

    
def clear_apple():
    global apple_position_y
    global apple_position_x
    terminal.print_at(apple_position_x, apple_position_y, ' ')

        

def checkPos(caudas, x, y):
    for x in range(len(caudas)):
        if(apple_position_x == caudas[x].x and apple_position_y == caudas[x].y):
            return True
    if(apple_position_x == x and apple_position_y == y):
        return True
    

def print_apple():
    
    terminal.print_at(apple_position_x, apple_position_y, f"{Fore.RED}H{Style.RESET_ALL}")
    