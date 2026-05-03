# Faz inputs para pegar 4 números com tratamento de erro
while True:
    try:
        n1 = int(input("Digite o 1° número: "))
        n2 = int(input("Digite o 2° número: "))
        n3 = int(input("Digite o 3° número: "))
        n4 = int(input("Digite o 4° e último número: "))
        break
    except ValueError:
        print("Digite um número válido inteiro!")
print('-='*22)
# Cria uma tupla com os números digitados
tupla_n = (n1, n2, n3, n4)

# Faz o print dos resultados
print(f"Você digitou os números {tupla_n}")

vezes9 = tupla_n.count(9)
if  vezes9 == 1:
    print(f"o número 9 apareceu {vezes9}ª vez")
else:
    print(f"o número 9 apareceu {vezes9} vezes")

if 3 in tupla_n:
    print(f"o número 3 apareceu na {(tupla_n.index(3))+1}ª posição ")
else:
    print("O número 3 não foi digitado em nenhuma posição.")

print(f"Os números pares digitados são: ", end="")
for n in tupla_n:
    if n % 2 == 0:
        print(n, end=' ')
