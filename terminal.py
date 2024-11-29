import sys

def print_at(x, y, char):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x + 1, y + 1, char))
    sys.stdout.flush()