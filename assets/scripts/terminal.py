import sys
import shutil
import asyncio

console_width = shutil.get_terminal_size().columns
console_height = shutil.get_terminal_size().lines

text_size = 0

def print_at(x, y, char):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, char))
    sys.stdout.flush()

def handle_resize():
    global console_width
    global console_height
    console_width = shutil.get_terminal_size().columns
    console_height = shutil.get_terminal_size().lines

def show_title(text):
    global text_size
    text_size = len(text)
    print_at(1,1, text)

def clear_title():
    global text_size
    clear = ""    
    for x in range(text_size):
        clear += chr(32)