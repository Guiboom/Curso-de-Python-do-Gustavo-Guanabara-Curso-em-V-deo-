menor=None
maior1k=total=0
while True:

    nome = input("Digite o nome do produto: ")

    while True:
        preco = input("Digite o preço do produto: ")
        try:
            preco=float(preco)
            break
        except ValueError:
            print(f"'{preco}' não é um número!")

    total+=preco

    if preco>1000:
        maior1k+=1

    if menor == None or preco < menor:
        menor = preco
        nomemenor=nome

    while True:
        chc= input('Você deseja continuar?(S/N): ').upper().strip()
        if chc=="S" or chc=="N":
            break
        else:
            print('A escolha é invalida!')

    if chc == 'N':
        break

print('-'*50)
print(f"""    Total gasto na compra: {total:.2f}
    Quantidade de produtos com preço maior que R$1000: {maior1k}
    Nome do produto mais barato: {nomemenor}""")
print('-'*50)
