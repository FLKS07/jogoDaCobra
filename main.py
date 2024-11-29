import cobra
import terminal
import os

cobra = cobra.Cobra(1,1)

cobra.heading = [1,1]

os.system('cls' if os.name == 'nt' else 'clear')
terminal.print_at(cobra.x, cobra.y, "Mongol")
