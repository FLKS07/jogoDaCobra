import sys

def print_at(x, y, char):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, char))
    sys.stdout.flush()