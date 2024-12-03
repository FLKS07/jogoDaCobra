import os
highscore_path = "../game_data/highscore.txt"
highScore = open(highscore_path).read()
os.system('cls' if os.name == 'nt' else 'clear') 

try:
    speed = float(input("Qual é a velocidade de jogo? Maior número menor velocidade(1 É Padrão): "))
except:
    speed = 1
speed = speed/10
input("Pressione ENTER quando a janela de jogo está pronta!")

import cobra
import terminal
import apples
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import sounds
import keyboard # type: ignore


import time

cobra = cobra.Cobra(1,1)
for x in range(0,3):
    cobra.addCaudas()

time.sleep(1)

heading = [0,0] #[X,Y]-

os.system('cls' if os.name == 'nt' else 'clear') # Limpa o ecrã

apples.generate_apple(cobra.caudas, cobra.x, cobra.y)



while True:
    terminal.handle_resize(cobra) 
    terminal.show_title(f"Points: {Fore.LIGHTBLUE_EX}{cobra.getPoints()}{Style.RESET_ALL}, HighScore: {Fore.YELLOW}{highScore}{Style.RESET_ALL},")
    heading = keyboard.heading
    cobra.changePosition(heading[0],heading[1])    
    terminal.print_at(cobra.x, cobra.y, f"{Fore.WHITE}O{Style.RESET_ALL}")
    apples.print_apple()
    time.sleep(speed)
    terminal.clear_title()
    if(cobra.checkDead() == True):
        break
os.system('cls' if os.name == 'nt' else 'clear') 

file = open(highscore_path, 'w')
file.write(str(cobra.getPoints()))

sounds.play_sound_file("..\\sounds\\game_over.wav")
os.system('cls' if os.name == 'nt' else 'clear') 
print("GameOver, press ENTER to EXIT the game!")
#input()

