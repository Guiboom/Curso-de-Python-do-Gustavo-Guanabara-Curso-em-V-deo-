# Declaração de classe
class Gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa< use
    variavel = Gafanhoto(nome, idade)
    """

    def __init__(self, nome="vazio", idade=0):  # Método Construtor
        # Atributos de Instâncias
        self.nome = nome
        self.idade = idade

    # Método de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome = {self.nome} : idade = {self.idade}"


# Declaração de objetos

g1 = Gafanhoto("GG", 70)
g2 = Gafanhoto("JJ", 17)
g3 = Gafanhoto()

g1.aniversario()
g2.aniversario()

print(g1.mensagem())
print(g2.mensagem())
print(g3.mensagem())

print(g1.__doc__)  # Dunder Attribute

print(g1)

print(g1.__dict__)  # Atribute

print(g1.__getstate__())  # Method

print(g1.__class__)