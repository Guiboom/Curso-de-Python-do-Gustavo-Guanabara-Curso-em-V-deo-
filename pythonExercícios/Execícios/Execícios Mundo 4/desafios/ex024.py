from abc import ABC, abstractmethod # Abstract Base Classes

class BebidaQuente(ABC):
    def preparar(self):
        print("")
        self.ferver_agua()
        self.misturar()
        self.servir()
        
    def ferver_agua(self):
        print("Fervendo água...")
        
    @abstractmethod
    def misturar(self):
        pass
        
    @abstractmethod
    def servir(self):
        pass
    
class Cafe(BebidaQuente):
    def misturar(self):
        print("Misturando o café com água quente...")
        
    def servir(self):
        print("Servindo o café na xícara...")
        
class Cha(BebidaQuente):
    def misturar(self):
        print("Misturando o chá com água quente...")
        
    def servir(self):
        print("Servindo o chá na xícara...")
        
class LeiteQuente(BebidaQuente):
    def misturar(self):
        print("Misturando o leite com água quente...")
        
    def servir(self):
        print("Servindo o leite quente na xícara...")
    
    
c1 = Cafe()
c1.preparar()


ch1 = Cha()
ch1.preparar()


l1 = LeiteQuente()
l1.preparar()
