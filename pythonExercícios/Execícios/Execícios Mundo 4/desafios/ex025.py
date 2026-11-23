from abc import ABC, abstractmethod # Abstract Base Classes

class Transporte(ABC):
    
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calcular_frete(self):
        pass
    
class Moto(Transporte):
    
    def __init__(self, distancia):
        super().__init__(distancia)
        self.FATOR=0.50 
    
    
    def calcular_frete(self):
        self.frete = self.distancia * self.FATOR 
        print(f"Valor do frete de {self.distancia}Km é R${self.frete}")

        
class Caminhao(Transporte):
    
    def __init__(self, distancia):
        super().__init__(distancia)
        self.FATOR=1.20
    
    
    def calcular_frete(self):
        if self.distancia<50:
            print("Indisponivel, Frete menor que 50Km")
            return
        self.frete = self.distancia * self.FATOR
        print(f"Valor do frete de {self.distancia}Km é R${self.frete}")
        
class Drone(Transporte):
    
    def __init__(self, distancia):
        super().__init__(distancia)
        self.FATOR=9.50 
    
    
    def calcular_frete(self):
        if self.distancia>10:
            print("Indisponivel, Frete maior que 10Km")
            return
        self.frete = self.distancia * self.FATOR
        print(f"Valor do frete de {self.distancia}Km é R${self.frete}")
        
    
""" e1= Moto(100)
e1.calcular_frete()

e2= Caminhao(500)
e2.calcular_frete()

e22= Caminhao(40)
e22.calcular_frete()

e3= Drone(10)
e3.calcular_frete()

e31= Drone(50)
e31.calcular_frete()
 """
