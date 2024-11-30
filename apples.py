import terminal
import random
import cobra

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


apple_position_x = 0
apple_position_y = 0

def generate_apple():
    global apple_position_x
    global apple_position_y

    apple_position_y = random.randrange(1,terminal.console_height)
    apple_position_x = random.randrange(1,terminal.console_width)

    while(cobra.Cobra.checkCoordineIsOcupied(apple_position_x,apple_position_y)):
        apple_position_y = random.randrange(1,terminal.console_height)
        apple_position_x = random.randrange(1,terminal.console_width)

    

def print_apple():
    
    terminal.print_at(apple_position_x, apple_position_y, f"{Fore.RED}H{Style.RESET_ALL}")
    