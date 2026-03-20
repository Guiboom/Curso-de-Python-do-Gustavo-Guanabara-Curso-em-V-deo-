#Faz inputs para pegar 4 números com tratamento de erro
while True:
    try:
        n1 = int(input("Digite o 1° número: "))
        n2 = int(input("Digite o 2° número: "))
        n3 = int(input("Digite o 3° número: "))
        n4 = int(input("Digite o 4° e último número: "))
        break
    except ValueError:
        print("Digite um número válido inteiro!")

#Cria uma tupla com os números digitados
tupla_n= (n1,n2,n3,n4)

#Pega cada número par a adiciona a lista 'pares'
pares = []
for n in tupla_n:
    if n % 2 == 0:
        pares.append(n)

#Faz o print para o usuario
print(f"o número 9 apareceu {tupla_n.count(9)} vez")

if 3 in tupla_n:
    print(f"o número 3 apareceu na posição {(tupla_n.index(3))+1}")
else:
    print("O número 3 não foi digitado em nenhuma posição.")

print(f"Os números pares digitados são: {pares}")