def leiaDinheiro(texto):
    while True:
        try:
            valor = float(input(f'{texto}'))
            return valor
        except:
            print("Valor não monetário!")
