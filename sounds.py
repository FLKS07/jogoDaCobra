from playsound import playsound
import threading



def play_sound_file(sound_file):
    thread = threading.Thread(target=playsound, args=(sound_file,), daemon=True)
    thread.start()


