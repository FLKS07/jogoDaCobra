speed = float(input("Qual é a velocidade de jogo? Maior número menor velocidade: "))
input("Pressione ENTER quando a janela de jogo está pronta!")

import cobra
import terminal
import keyboard
import apples
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

import os
import time

cobra = cobra.Cobra(1,1)
for x in range(0,3):
    cobra.addCaudas()

time.sleep(1)

heading = [0,0] #[X,Y]

os.system('cls' if os.name == 'nt' else 'clear') # Limpa o ecrã

apples.generate_apple()



while True:
    terminal.handle_resize()
    
    terminal.show_title(f"Points: {cobra.getPoints()}")
    heading = keyboard.heading
    cobra.changePosition(heading[0],heading[1])

    
    terminal.print_at(cobra.x, cobra.y, f"{Fore.WHITE}O{Style.RESET_ALL}")
    

    apples.print_apple()
    time.sleep(speed)

    terminal.clear_title()
    if(cobra.checkDead() == True):
        break
os.system('cls' if os.name == 'nt' else 'clear') 
print("GameOver")


