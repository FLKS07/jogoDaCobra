import cobra
import terminal
import os
import time

cobra = cobra.Cobra(1,1)
time.sleep(1)

heading = [1,1]

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    terminal.print_at(cobra.x, cobra.y, "0")
    cobra.changePosition(1,1)
    time.sleep(1)
