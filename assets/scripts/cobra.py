import terminal
import apples
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import sounds




class Cobra:
    def __init__(self, x, y): 
        self.x = x # Componente de posição X
        self.y = y # Componente de posição y
        self.caudas = [] # A lista de caudas

        self.last_position_x = 0 # Qual foi a última posição
        self.last_position_y = 0

        #print(f"Y: {terminal.console_height} X: {terminal.console_width}")

    def changePosition(self, x,y): # A função par mudar a posição
        self.last_position_x = self.x # Antes de mudar a posição recorda a posição atual
        self.last_position_y = self.y
       
        self.x += x # Muda a posição
        self.y += y
        

        # Se a posição da cebeça da cobra passar os limites do terminal muda para baixo ou para cima, dependendo
        if self.x > terminal.console_width:
            self.x = 1  # Wrap to the start
        elif self.x <= 0:
            self.x = terminal.console_width

        if self.y > terminal.console_height:
            self.y = 2
        elif self.y <= 1:
            self.y = terminal.console_height
        
        for tail in self.caudas: # Limpa no terminal as caudas 
            tail.clear_self()

        for i in range(0, len(self.caudas)): # Muda a posição das caudas
            if(i == 0):
                self.caudas[0].changePosition(self.last_position_x, self.last_position_y) # Muda a primeira cauda para a posição anterior da cabeça da cobra
            else:
                self.caudas[i].changePosition(self.caudas[i - 1].last_position_x, self.caudas[i - 1].last_position_y) # Muda com a posição anterior da seguinte cauda


        # Show the tails on the screen
        for tail in self.caudas: # Mostra a cauda no ecrã de jogo
            tail.show_screen()

        if(apples.apple_position_x == self.x and apples.apple_position_y == self.y): # Se a cabeça da corda estiver na posição de uma maçã faz o código abaixo
            sounds.play_sound_file("../sounds/pickup.wav") # Toca o som de pickup
            Cobra.addCaudas(self) # Adiciona uma cauda
            apples.generate_apple(self.caudas, self.x, self.y) # E spawna uma maçã aleotoriamente no jogo

        
        #print(f"New position: X = {self.x}, Y = {self.y}")

    def addCaudas(self): # Código para adicionar as caudas
        self.caudas.append(Cauda(self.last_position_x, self.last_position_y)) # Adiciona a cauda
    
    def getPoints(self):
        return len(self.caudas) # Vai buscar quantas caudas a cobra tem
    
    def checkDead(self): # Código para ver se a cobra morreu
        for x in range(len(self.caudas)): # Vai buscar ás caudas se a poisção da cabeça da cobra é igual á posição das caudas todas
            if(self.x == self.caudas[x].x and self.y == self.caudas[x].y):
                return True # Devolve verdade se isso acontecer
        return False # Senão diz que não está na cabeça das caudas
    
    def checkCoordineIsOcupied(self,x,y): # Este código é para verificar se uma coordenada está a ser ocupada pela a cobra
        if(x == self.x and y == self.y): # Se a coordenada for igual á posição da cobra devolve verdade
            return True
        else: # Se não for igual vai verificar se as caudas ocupam essa posição
            for x in range(len(self.caudas)): 
                if(self.caudas[x].x == self.x and y == self.caudas[x].y):
                    return True
            return False # Se nada ocupar devolve falso

class Cauda: # O Objeto ca Cauda
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
    def clear_self(self): # Limpa a cauda no terminal
        terminal.print_at(self.x, self.y, chr(32))
    def show_screen(self): # Mostra a cauda na linha de comandos
        terminal.print_at(self.x, self.y, f"{Fore.GREEN}█{Style.RESET_ALL}")
        
    
    