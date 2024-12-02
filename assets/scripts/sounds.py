from playsound import playsound
import threading



def play_sound_file(sound_file):
    threading.Thread(target=playsound, args=(sound_file,), daemon=True).start()



