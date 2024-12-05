from playsound import playsound
import threading


def play_sound_file(sound_file):
    threading.Thread(target=playsound, args=(sound_file,), daemon=True).start()
    # Cria uma thread, ou seja, parecido com um programa novo para tocar o som uma vez,
    # isto foi feito porque sem isto o código ia esperar que o som terminasse de tocar
    
def play_loop(sound_file): # Vai chamar a função play com uma thread
    threading.Thread(target=play, args=(sound_file,), daemon=True).start()
    
def play(sound_file):
    while True: # Enquanto for verdade vai tocar a música
        playsound(sound_file)
