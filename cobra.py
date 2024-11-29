import shutil

console_width = shutil.get_terminal_size().columns
console_height = shutil.get_terminal_size().lines

class Cobra:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        print(f"Y: {console_height} X: {console_width}")

    def changePosition(self, x,y):
       # Increment the position
        self.x += x
        self.y += y
        

        # Wrap around if the position goes beyond the console width or height
        if self.x > console_width:
            self.x = 1  # Wrap to the start
        if self.y > console_height:
            self.y = 1
        print(f"New position: X = {self.x}, Y = {self.y}")