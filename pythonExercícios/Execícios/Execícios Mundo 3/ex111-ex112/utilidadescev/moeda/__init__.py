# aumentar, diminir, dobro, metade


def aumentar(valor, aument, form=False):
    """funct aumentar
    :valor == valoridade do valor a ser aumentado
    :aument == aumento em porcentagem
    """
    valor = ((valor / 100) * aument) + valor
    if form == True:
        valor = moeda(valor)
    return valor


def diminuir(valor, dimin, form=False):
    """funct diminuir
    :valor == valoridade do valor a ser diminuido
    :aument == diminuição em porcentagem
    """
    valor = valor - ((valor / 100) * dimin)
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
    valor = f"R${valor:_.2f}".replace(".", ",").replace("_",".")
    return valor


def resumo(valor, aumento, reducao):
    """_summary_

    Args:
        valor (str): valor a ser usado como base nos calculos
        aumento (str): aumento em %
        redu (str): redução em %
    """
    print(f"-" * 35)
    print("RESUMO DO VALOR".center(35))
    print(f"-" * 35)
    print(f"Preço analisado:".ljust(20), moeda(valor))
    print(f"Dobro do preço:".ljust(20, " "), dobro(valor, form=True))
    print(f"Metade do preço:".ljust(20, " "), metade(valor, form=True))
    print(f"{aumento}% de aumento:".ljust(20, " "), aumentar(valor, aumento, form=True))
    print(f"{reducao}% de redução:".ljust(20, " "), diminuir(valor, reducao, form=True))
    print(f"-" * 35)
