import cobra
import terminal
import keyboard

import os
import time

cobra = cobra.Cobra(1,1)
cobra.addCaudas()
cobra.addCaudas()
cobra.addCaudas()
cobra.addCaudas()
cobra.addCaudas()
cobra.addCaudas()

time.sleep(1)

heading = [0,0] #[X,Y]




while True:
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa o ecrã
    heading = keyboard.heading
    cobra.changePosition(heading[0],heading[1])
    terminal.print_at(cobra.x, cobra.y, "0")
    time.sleep(0.3)
