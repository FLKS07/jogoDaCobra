from pynput import keyboard as pkeyboard

# A set to track pressed special keys
pressed_keys = set()
heading = [0, 1]

def on_press(key):
    global heading
    
        # Check for character keys
    if key.char == 'a':
        heading = [-1, 0]
    elif key.char == 'd':
        heading = [1, 0]
    elif key.char == 'w':
        heading = [0, -1]
    elif key.char == 's':
        heading = [0, 1]
        



# Start the listener in the background
listener = pkeyboard.Listener(on_press=on_press)
listener.start()