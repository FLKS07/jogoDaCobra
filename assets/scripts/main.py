import os
import cobra
import terminal
import apples
from colorama import Fore
from colorama import Style
from colorama import Back
import sounds
import keyboard_my
import time

highscore_path = "../game_data/highscore.txt"
highScore = int(open(highscore_path).read())
os.system('cls' if os.name == 'nt' else 'clear') 
with_music = False

try:
    input_ = input("Quer música? sim ou não (Não é padrão): ")
    if(input_ == "sim"):
        with_music = True
except:
    pass


try:
    speed = float(input("Qual é a velocidade de jogo? Maior número menor velocidade(1 É Padrão): "))
except:
    speed = 1
speed = speed/10
input("Pressione ENTER quando a janela de jogo está pronta!")



cobra = cobra.Cobra(1,1)
for x in range(0,3):
    cobra.addCaudas()

time.sleep(1)

heading = [0,0] #[X,Y]-

os.system('cls' if os.name == 'nt' else 'clear') # Limpa o ecrã



terminal.move_cursor_off_screen(10000, 10000)

def title():
    title_size = len("Points: ") + len(" HighScore:") + len(str(cobra.getPoints())) + len(str(highScore))
    title = f"{Back.LIGHTBLACK_EX}Points: {Fore.LIGHTBLUE_EX}{cobra.getPoints()}{Style.RESET_ALL}{Back.LIGHTBLACK_EX} HighScore: {Fore.YELLOW}{highScore}{Style.RESET_ALL}"
    title += f"{Back.LIGHTBLACK_EX}"
    for x in range(0,terminal.console_width - title_size - 1):
        title += " "
    title += f"{Style.RESET_ALL}"
    return title
        
apples.generate_apple(cobra.caudas, cobra.x, cobra.y)

if(with_music == True):
    sounds.play_loop("../sounds/waterfall.mp3")

while True:
    terminal.handle_resize(cobra) 
    terminal.show_title(title())
    heading = keyboard_my.heading
    cobra.changePosition(heading[0],heading[1])    
    terminal.print_at(cobra.x, cobra.y, f"{Fore.WHITE}O{Style.RESET_ALL}")
    time.sleep(speed)
    
    if(cobra.checkDead() == True):
        break

keyboard_my.listener.stop()
os.system('cls' if os.name == 'nt' else 'clear') 

points = cobra.getPoints()
 
if(points > highScore):
    file = open(highscore_path, 'w')
    file.write(str(points))
    file.close

sounds.play_sound_file("../sounds/game_over.wav")
os.system('cls' if os.name == 'nt' else 'clear') 
print("GameOver, press ENTER to EXIT the game!") 
input()


