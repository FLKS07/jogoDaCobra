import shutil
import terminal


console_width = shutil.get_terminal_size().columns
console_height = shutil.get_terminal_size().lines


class Cobra:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__caudas = []

        self.last_position_x = 0
        self.last_position_y = 0

        print(f"Y: {console_height} X: {console_width}")

    def changePosition(self, x,y):
        self.last_position_x = self.x
        self.last_position_y = self.y
       
        self.x += x
        self.y += y
        

        # Wrap around if the position goes beyond the console width or height
        if self.x > console_width:
            self.x = 1  # Wrap to the start
        elif self.x <= 0:
            self.x = console_width

        if self.y > console_height:
            self.y = 1
        elif self.y <= 0:
            self.y = console_height
        

        for i in range(0, len(self.__caudas)):
            if(i == 0):
                self.__caudas[0].changePosition(self.last_position_x, self.last_position_y) 
            else:
                self.__caudas[i].changePosition(self.__caudas[i - 1].last_position_x, self.__caudas[i - 1].last_position_y)


        # Show the tails on the screen
        for tail in self.__caudas:
            tail.show_screen()


        
        #print(f"New position: X = {self.x}, Y = {self.y}")

    def addCaudas(self):
        self.__caudas.append(Cauda(self.last_position_x, self.last_position_y))

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
    def show_screen(self):
        terminal.print_at(self.x, self.y, "A")
    
    