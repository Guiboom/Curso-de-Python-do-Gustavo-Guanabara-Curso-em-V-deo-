from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, quant=0):
        self.quant = quant
    def analisar(self):
     return Panel(f"""
Analisando o Churrasco com {self.quant} convidados
Cada participante comerá 0.4kg e cada Kg custa R$82.40
Recomendo comprar {self.quant *0.4}Kg de carne
O custo total será de R${self.quant *0.4 *82.40:.2f}
Cada pessoa pagará R${(self.quant *0.4 *82.40)/self.quant:.2f}
                                """, title="Churrasco" )

p1 = Churrasco(15)
print(p1.analisar())
