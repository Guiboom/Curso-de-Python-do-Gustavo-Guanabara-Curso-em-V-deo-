from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome="", preco=0.00):
        self.nome = nome
        self.preco = preco
    
    def etiqueta(self):
                
        produto = Panel(f"""
        {self.nome}
        {self.preco}
                        """, title="Produto" )
        
        return produto
    
    
p1 = Produto("Notebook", 4000)
p2 = Produto("Smartphone", 2500)

print(p1.etiqueta())
print(p2.etiqueta())