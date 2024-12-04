from playsound import playsound
import threading


def play_sound_file(sound_file):
    threading.Thread(target=playsound, args=(sound_file,), daemon=True).start()
    
def play_loop(sound_file):
    threading.Thread(target=play, args=(sound_file,), daemon=True).start()
    
def play(sound_file):
    while True:
        playsound(sound_file)
