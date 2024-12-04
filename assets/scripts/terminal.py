import sys
import shutil
import apples
import os

console_width = shutil.get_terminal_size().columns
console_height = shutil.get_terminal_size().lines

text_size = 0

def print_at(x, y, char):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, char))
    sys.stdout.flush()

def handle_resize(cobra):
    global console_width
    global console_height

    last_console_width = console_width
    last_console_height = console_height

    console_width = shutil.get_terminal_size().columns
    console_height = shutil.get_terminal_size().lines

    if(last_console_height != console_height or last_console_width != console_width):
        os.system('cls' if os.name == 'nt' else 'clear') 
        apples.clear_apple()
        apples.generate_apple(cobra.caudas, cobra.x, cobra.y)
        

def show_title(text):
    global text_size
    text_size = len(text)
    print_at(1,1, text)

def hide_cursor():
    sys.stdout.write("\x1b[?25l")
    sys.stdout.flush()

def move_cursor_off_screen(x, y):
    # Moves the cursor to a specific (x, y) position, out of view if desired
    sys.stdout.write(f"\x1b[{y};{x}H")
    sys.stdout.flush()