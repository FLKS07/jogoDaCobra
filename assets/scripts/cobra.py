import terminal
import apples
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import sounds




class Cobra:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.caudas = []

        self.last_position_x = 0
        self.last_position_y = 0

        #print(f"Y: {terminal.console_height} X: {terminal.console_width}")

    def changePosition(self, x,y):
        self.last_position_x = self.x
        self.last_position_y = self.y
       
        self.x += x
        self.y += y
        

        # Wrap around if the position goes beyond the console width or height
        if self.x > terminal.console_width:
            self.x = 1  # Wrap to the start
        elif self.x <= 0:
            self.x = terminal.console_width

        if self.y > terminal.console_height:
            self.y = 2
        elif self.y <= 1:
            self.y = terminal.console_height
        
        for tail in self.caudas:
            tail.clear_self()

        for i in range(0, len(self.caudas)):
            if(i == 0):
                self.caudas[0].changePosition(self.last_position_x, self.last_position_y) 
            else:
                self.caudas[i].changePosition(self.caudas[i - 1].last_position_x, self.caudas[i - 1].last_position_y)


        # Show the tails on the screen
        for tail in self.caudas:
            tail.show_screen()

        if(apples.apple_position_x == self.x and apples.apple_position_y == self.y):
            sounds.play_sound_file("../sounds/pickup.wav")
            Cobra.addCaudas(self)
            apples.generate_apple(self.caudas, self.x, self.y)

        
        #print(f"New position: X = {self.x}, Y = {self.y}")

    def addCaudas(self):
        self.caudas.append(Cauda(self.last_position_x, self.last_position_y))
    
    def getPoints(self):
        return len(self.caudas)
    
    def checkDead(self):
        for x in range(len(self.caudas)):
            if(self.x == self.caudas[x].x and self.y == self.caudas[x].y):
                return True
        return False
    
    def checkCoordineIsOcupied(self,x,y):
        if(x == self.x and y == self.y):
            return True
        else:
            for x in range(len(self.caudas)):
                if(self.caudas[x].x == self.x and y == self.caudas[x].y):
                    return True
            return False

class Cauda:
    def changePosition(self, x, y):
        self.last_position_x = self.x
        self.last_position_y = self.y

        self.x = x
        self.y = y

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.last_position_x = self.x
        self.last_position_y = self.y
    def clear_self(self):
        terminal.print_at(self.x, self.y, chr(32))
    def show_screen(self):
        terminal.print_at(self.x, self.y, f"{Fore.GREEN}A{Style.RESET_ALL}")
        
    
    