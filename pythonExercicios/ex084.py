#listas
pessoa = list()
pessoaS = list()
pesados = list()
leves = list()

while True:

    #Adiciona nome e peso a lista pessoa
    pessoa.append(input("Digite o nome da pessoa: ")) #pessoa[0]=nome
    pessoa.append(int(input("Digite o peso da pessoa: "))) #pessoa[1]=peso

    #Adiciona uma copia da lista pessoa a lista pessoaS
    pessoaS.append(pessoa[:])

    #Se for a primeira pessoa adicionadad ele define que ela tem o maior e menor peso
    if len(pessoaS) == 1:
        maiorpeso = menorpeso = pessoa[1]

    else:
        #Se o peso da pessoa for maior do que o valor maiorpeso ele substitui
        if pessoa[1] > maiorpeso:
            maiorpeso = pessoa[1]

        #Se o peso da pessoa for menor do que o valor menorpeso ele substitui
        if pessoa[1] < menorpeso:
            menorpeso = pessoa[1]

    #Limpa a lista pessoa
    pessoa.clear()

    #Pergunta se deseja continuar
    chc = (input("Você deseja continuar? S/N: ")).upper()
    if chc == 'N':
        break

# Verifica se na lista pessoaS tem pessoas com o peso igual ao maiorpeso e menorpeso, caso tenha ele adiciona o nome
for p in pessoaS:
    if p[1] == maiorpeso:
        pesados.append(p[0])

    if p[1] == menorpeso:
        leves.append(p[0])

#Organizador
print("=-="*20)

#Mostra o pedido
print(f'Foram cadastradas {len(pessoaS)} pessoas')
print(f'Pessoas mais pesadas {pesados} com {maiorpeso}kg')
print(f'Pessoas mais leves {leves} com {menorpeso}kg')
