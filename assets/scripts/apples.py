import terminal
import random

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


apple_position_x = 0
apple_position_y = 0

def generate_apple(caudas, x, y): # Código para spawnar a cauda numa posição qualquer
    global apple_position_x
    global apple_position_y

    apple_position_y = random.randrange(2,terminal.console_height) # Vai buscar um X aleatório entre 2 (o 2 é por causa do título) e a altura da linha de comandos
    apple_position_x = random.randrange(1,terminal.console_width)# Vai buscar um Y aleatório entre 1 e a altura da linha de comandos

    
    
    while(checkPos(caudas,x,y)): # Quando a função der verdadeiro vai gerar este código infinito
        apple_position_y = random.randrange(2,terminal.console_height) # O mesmo de acima
        apple_position_x = random.randrange(1,terminal.console_width)

    print_apple() # Mostra a maçã na linha de comandos

    
def clear_apple(): # Limpa a maçã
    global apple_position_y
    global apple_position_x
    terminal.print_at(apple_position_x, apple_position_y, ' ')

        

def checkPos(caudas, x, y): # O código para verificar se a posição está ocupada igual á da cobra
    global apple_position_x
    global apple_position_y
    
    for cauda in caudas:
        if cauda.x == apple_position_x and cauda.y == apple_position_y:
            return True
        if x == apple_position_x and y == apple_position_x:
            return True
    return False
    

def print_apple(): # Mostra a maçã na linha de comandos
    terminal.print_at(apple_position_x, apple_position_y, f"{Fore.RED}█{Style.RESET_ALL}")
    