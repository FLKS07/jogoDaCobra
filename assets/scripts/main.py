import os #Para falar com o kernel do sistema operativo
import cobra #O módulo feito pelo o grupo da cobra onde está o código para controlar a cobra
import terminal #O módulo feito peolo o grupo para saber várias característiscas sobre a linha de comandos
import apples #O módulo da maçã para controlar os spawns das maçãs
from colorama import Fore
from colorama import Style # Módulos para mudar a cor do bacgrkound e das letras dos caracteres
from colorama import Back
import sounds #Módulo feito pelo o grupo para tocar música
import keyboard_my #Módulo feito pelo o grupo para saber quais são as teclas do teclado para controlar a cobra
import time # Módulo para parar o programa em um determinado tempo
import sys # Módulo para mudar certas coisa sobre a linha de comandos

highscore_path = "../game_data/highscore.txt" # Saber onde o ficheiro do recorde está guardado

try:
    highScore = int(open(highscore_path).read()) #Ler o ficheiro do recorde
except:
    highScore = 0 # Se esse ficheiro não existir o recorde vai ser 0
with_music = False # Valor padrão para saber se o jogador quer jogar com música


os.system('cls' if os.name == 'nt' else 'clear') #Limpar o ecrã
try:
    input_ = input("Quer música? sim ou não (Não é padrão): ") # Pergunta ao jogador para saber se ele quer música
    if(input_.lower() == "sim"): # Coverte a respostas para letras maísculas e se for sim o jogo é jogado com música
        with_music = True # O programa agora vai tocar com música
except:
    pass #Se o jogador meter outra coisa qualquer o valor não vai mudar


try:
    speed = float(input("Qual é a velocidade de jogo? Maior número menor velocidade(1 É Padrão): ")) # Aqui o jogador é perguntado qual é a velocidade do jogo
except:
    speed = 1 # Se não for dado um valor inválido a velocidade vai ser 1
speed = speed/10 # Aqui a velocidade é dividida por exemplo se for 1 s vai ser convertida para 100 ms
input("Pressione ENTER quando a janela de jogo está pronta!") # Aqui pede ao jogador para se preperar



cobra = cobra.Cobra(1,2) # Posição inical da cobra
for x in range(0,3): # Adidciona 3 caudas á cobra
    cobra.addCaudas() # A função para adicionar cobras


time.sleep(1) # Espera 1 segundo

heading = [0,0] # O vetor da direção, ou seja v = 0ex, 0ey

os.system('cls' if os.name == 'nt' else 'clear') # Limpa o ecrã



terminal.move_cursor_off_screen(10000, 10000) # Remover o cursor do terminal fora do ecrã dele

def title(): # Função para o título de jogo
    title_size = len("Points: ") + len(" HighScore:") + len(str(cobra.getPoints())) + len(str(highScore)) # Calcula o tamanho do título
    title = f"{Back.LIGHTBLACK_EX}Points: {Fore.LIGHTBLUE_EX}{cobra.getPoints()}{Style.RESET_ALL}{Back.LIGHTBLACK_EX} HighScore: {Fore.YELLOW}{highScore}{Style.RESET_ALL}"
    # Alinha acima é uma string com o título com as cores incluídas
    title += f"{Back.LIGHTBLACK_EX}"
    for x in range(0,terminal.console_width - title_size - 1):
        title += " " # Adicina espaços vazios ao título para que ele mostre uma linha a cinzento
    title += f"{Style.RESET_ALL}" 
    return title # Devolve o título com os espaços vazius a cizento
        
apples.generate_apple(cobra.caudas, cobra.x, cobra.y) # Gera uma maçã sabendo as coordenadas da cauda e da cabeça da cobra

if(with_music == True): # Se o jogador ter decidido que quer jogar com música joga com música
    sounds.play_loop("../sounds/waterfall.mp3") # Este código é para tocar música em loop, ou seja, nunca acabar

while True: # Lógica principal do jogo
    terminal.handle_resize(cobra) # Se o jogador mudar o tamanho da terminal esta função irá tratar disso
    terminal.show_title(title()) # Mostra o título no terminal
    heading = keyboard_my.heading # Vais buscar a direção ao módulo keyboard_my feita pelo o grupo
    cobra.changePosition(heading[0],heading[1]) # Vai adicionar o vetor de posição da cobra com o vetor da direção buscada na linha acima
    terminal.print_at(cobra.x, cobra.y, f"{Fore.WHITE}O{Style.RESET_ALL}") #Mostra no terminal a cabeça da cobra a branco
    time.sleep(speed) # Espera pelo o tempo defenido pelo o jogador a cima
    
    if(cobra.checkDead() == True):
        break

keyboard_my.listener.stop() # Para de "escutar" clicks do teclado
os.system('cls' if os.name == 'nt' else 'clear') #Limpa o ecrã para limpar a área do jogo

points = cobra.getPoints() # Vai buscar os pontos á cobra que é apenas quantas caudas a cobra tem
 
if(points > highScore): # Se os pontos serem melhores que o recorde vai escrever um ficheiro com os pontos
    file = open(highscore_path, 'w') # Aqui o programa abre o ficheiro
    file.write(str(points)) # Aqui o programa escreve o ficheiro
    file.close # Aqui fecha o ficheiro

sounds.play_sound_file("../sounds/game_over.wav") #Aqui toca o som de game over
os.system('cls' if os.name == 'nt' else 'clear') # Limpa o ecrã

if(highScore < cobra.getPoints()): # Se o recorde for menor com os pontos obtidos escreve na linha de comandos a pontuação
    print(f"Melhor pontuação!\nNovo recorde:{Fore.YELLOW}{cobra.getPoints()}{Style.RESET_ALL}")
else:
    print(f"Pontuação:{Fore.LIGHTBLUE_EX}{cobra.getPoints()}{Style.RESET_ALL} Recorde:{Fore.YELLOW}{highScore}{Style.RESET_ALL}")
    # Se não escreve na linha de comandos quantos pontos foram obtidos e qual era o recorde

    
sys.stdout.flush() # Limpa o buffer de input da linha de comandos
print(f"\n{Fore.LIGHTRED_EX}GameOver{Style.RESET_ALL} Pressiona o ENTER para fechar o jogo")
input() # Quando o utlizador clicar no ENTER fecha o programa


