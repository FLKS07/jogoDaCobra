class Cobra:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.heading = [1,0]
    

    def changeHeading(self, x,y):
        self.heading = [x, y]
        