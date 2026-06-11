#aumentar, diminir, dobro, metade

def aumentar(valor, aument, form=False):
    """funct aumentar
    :valor == valoridade do valor a ser aumentado
    :aument == aumento em porcentagem
    """
    valor = ((valor/100)*aument)+valor
    if form == True:
        valor = moeda(valor)
    return valor

def diminuir(valor, dimin, form=False):
    """funct diminuir
    :valor == valoridade do valor a ser diminuido
    :aument == diminuição em porcentagem
    """
    valor = valor-((valor/100)*dimin)
    if form == True:
        valor = moeda(valor)
    return valor

def dobro(valor, form=False):
    """funct dobro
    :valor == valor a ser dobrado
    """
    valor *= 2
    if form == True:
        valor = moeda(valor)
    return valor

def metade(valor, form=False):
    """funct metade
    :valor == valor a ser reduzido pela metade
    """
    valor /= 2
    if form == True:
        valor = moeda(valor)
    return valor

def moeda(valor):
    """funct moeda
    :valor == valor formatado str
    """
    valor = f"R${valor:.2f}".replace('.', ',')
    return valor
    