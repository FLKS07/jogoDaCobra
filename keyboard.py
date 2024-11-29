import cobra
from pynput import keyboard as pkeyboard



pressed_keys = set()
heading = [0,1]


def on_press(key):
    global heading
    try:
        if(key.char == 'a'):
            heading = [-1, 0]
        elif(key.char == 'd'):
            heading = [1,0]
        elif(key.char == 'w'):
            heading = [0,-1]
        elif(key.char == 's'):
            heading = [0,1]          


        
    except AttributeError:
        pressed_keys.add(key)  # Add special keys
        print("Cannot find key")

def on_release(key):
    try:
        pressed_keys.remove(key.char)
    except AttributeError:
        pressed_keys.remove(key)  # Remove special keys
    if key == pkeyboard.Key.esc:
        return False



listener = pkeyboard.Listener(on_press=on_press)
listener.start()