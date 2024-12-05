from pynput import keyboard as pkeyboard # Importa a funcionalidades para detetar as teclas
from pynput.keyboard import Key

heading = [0, 1] # O vetor de direção inicial

def on_press(key): # O código quando o jogador pressiona uma tecla qualquer
    global heading # Para ir buscar a variável heading
    
    last_heading = heading # A last_heading vai ser igual á heading
    
    # Estes ifs é para detetar qual foi a tecla que o jogador pressionou e mudar o vetor de direção da tecla
    if key == Key.left:
        heading = [-1, 0]
    elif key == Key.right:
        heading = [1, 0]
    elif key == Key.up:
        heading = [0, -1]
    elif key == Key.down:
        heading = [0, 1]

    if(last_heading[0] == heading[0] *-1 or last_heading[1] == heading[1] *-1): # Se o vetor de direção tiver o sentido contrário e a mesma direção vai ficar com
        heading = last_heading # o mesmo vetor de direção
# Start the listener in the background
listener = pkeyboard.Listener(on_press=on_press) # O código para Escutar as teclas
listener.start() # O escutar é ativado
