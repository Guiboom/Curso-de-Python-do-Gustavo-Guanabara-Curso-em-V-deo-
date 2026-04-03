#Cria um lista
lista = []
posicoes_maiores = []
posicoes_menores = []

#Pede para o usuario digitar 5 vezes alguns números adicionandos a um lista
for i in range(5):
    lista.append(int(input('Digite um número: ')))
    
# Define o maior e menor número
maior_numero = max(lista)
menor_numero = min(lista)

for i, x in enumerate(lista):
    # Se o valor atual for igual ao maior ou menor valor encontrado...
    if x == maior_numero:
        # ...adicionamos a posição (índice) na nossa lista
        posicoes_maiores.append(i+1)
    if x == menor_numero:
        # ...adicionamos a posição (índice) na nossa lista
        posicoes_menores.append(i+1)

# Pra deixar mais organizado
print('-=-'*30)

# Dá um print mostrando os valores digitados, o maior e menor número digitado e q posição de cada
print(f'Você digitou os valores {lista}')
print(f'O maior número digitado foi {maior_numero} que está na posição {posicoes_maiores}')
print(f'O menor número digitado foi {menor_numero} que está na posição {posicoes_menores}')
