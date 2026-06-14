def leiaDinheiro(texto):
    while True:
        try:
            valor = float(input(f'{texto}').replace(",",".").strip().replace(" ", ""))
            return valor
        except:
            print("Valor não monetário!")
