#aumentar, diminir, dobro, metade

def aumentar(valor, aument):
    """funct aumentar
    :valor == valoridade do valor a ser aumentado
    :aument == aumento em porcentagem
    """
    valor = ((valor/100)*aument)+valor
    return valor

def diminuir(valor, dimin):
    """funct diminuir
    :valor == valoridade do valor a ser diminuido
    :aument == diminuição em porcentagem
    """
    valor = valor-((valor/100)*dimin)
    return valor

def dobro(valor):
    """funct dobro
    :valor == valor a ser dobrado
    """
    valor *= 2
    return valor

def metade(valor):
    """funct metade
    :valor == valor a ser reduzido pela metade
    """
    valor /= 2
    return valor