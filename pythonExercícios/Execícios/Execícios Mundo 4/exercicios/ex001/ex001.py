# Declaração de classe
class Gafanhoto:
    def __init__(self):  # Método Construtor
        # Atributos de Instâncias
        self.nome = ""
        self.idade = 0

    # Método de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."


# Declaração de objetos

g1 = Gafanhoto()
g2 = Gafanhoto()

#Atributos
g1.nome = "GG" 
g1.idade = 70 

#Métodos
g1.aniversario() 
print(g1.mensagem())

#Atributos
g2.nome = "JJ" 
g2.idade = 16 

#Métodos
g2.aniversario() 
print(g2.mensagem())
