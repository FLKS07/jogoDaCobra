from pynput import keyboard as pkeyboard

heading = [0, 1]

def on_press(key):
    global heading
    
    try:
        if key.char == 'a':
            heading = [-1, 0]
        elif key.char == 'd':
            heading = [1, 0]
        elif key.char == 'w':
            heading = [0, -1]
        elif key.char == 's':
            heading = [0, 1]
    except AttributeError:
        # Handle special keys here if needed (e.g., arrows, etc.)
        pass

# Start the listener in the background
listener = pkeyboard.Listener(on_press=on_press)
listener.start()