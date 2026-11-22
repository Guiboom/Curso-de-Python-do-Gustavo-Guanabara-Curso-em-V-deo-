from abc import ABC, abstractmethod # Abstract Base Classes


class Poligonos():
    def __init__(self, qtd_lados=0):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self, *lados):
        pass
    
    @abstractmethod
    def area(self):
        pass
    
class Quadrado(Poligonos):
    def __init__(self, lado=0):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2
    
class Circulo(Poligonos):
    def __init__(self, raio=0):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * 3.14 * self.raio

    def area(self):
        return 3.14 * (self.raio ** 2)
    
    
q1=Quadrado(5)
print(f"Perímetro do quadrado: {q1.perimetro()}")
print(f"Área do quadrado: {q1.area()}")
print(f"Lados do quadrado: {q1.qtd_lados}")

c1=Circulo(3)
print(f"Perímetro do círculo: {c1.perimetro()}")
print(f"Área do círculo: {c1.area()}")
print(f"Lados do círculo: {c1.qtd_lados}")