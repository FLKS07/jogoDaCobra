import sys
import shutil
import apples
import os

console_width = shutil.get_terminal_size().columns # Vai buscar a largura da linha de comandos
console_height = shutil.get_terminal_size().lines # Vai buscar a altura da linha de comandos

text_size = 0

def print_at(x, y, char):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, char)) # Este é o código para dar print do quer que seja numa posição qualquer da linha de comandos
    sys.stdout.flush() # Este é o código para dar print

def handle_resize(cobra):
    global console_width # Vai buscar a largura e altura
    global console_height

    last_console_width = console_width # a última largura é igual á largura da consola
    last_console_height = console_height# a última altura é igual á altura da consola

    console_width = shutil.get_terminal_size().columns # Vai buscar novamente a largura da consola
    console_height = shutil.get_terminal_size().lines # Vai buscar novamente a altura da conolsa

    if(last_console_height != console_height or last_console_width != console_width): # Se a última largura ou altura for diferente á altura e largura
        os.system('cls' if os.name == 'nt' else 'clear') # Lima o ecrã para não haver nenhuns artefactos
        apples.generate_apple(cobra.caudas, cobra.x, cobra.y) # Vai spawnar outra maçã qualquer
        

def show_title(text): # Mostra o título de jogo (aquele com os pontos)
    global text_size # Vai buscar qual é o tamanho do título (as letras)
    text_size = len(text) # O código para verificar o tamango do título
    print_at(1,1, text) # E dar print ao titulo de jogo na posição 1,1

def hide_cursor(): #Código para mudar o cursor de posição fora do terminal
    sys.stdout.write("\x1b[?25l")
    sys.stdout.flush()

def move_cursor_off_screen(x, y): #Código para mudar o cursor de posição fora do terminal
    sys.stdout.write(f"\x1b[{y};{x}H")
    sys.stdout.flush()