# Cria uma lsita
numeros = []

# Avisa ao usuário como parar o código
print('Para parar digite "pare"!')

# Um laço criado para adicionar numeros não adicionados ainda à lista até que ele digite 'pare' ou 'PARE'
while True:

    # Pede ao usuário digitar um número
    resposta = input("Digite um número: ")

    try:
        # Se ele digitar "pare" ou "PARE" ou " pare " ele para :)
        if resposta.upper().strip() == "PARE":
            break

        # Senão ele transforma em inteiro e adiciona a lista
        else:
            resposta = int(resposta)
            numeros.append(resposta)

    # Lida com erros de usuário
    except:
        print("Digite um valor inteiro ou resposta válida(pare)!")

# Cria uma lista ordenada de forma decrescente
numeros_orde_reve = sorted(numeros, reverse=True)

#Para deixar mais organizado
print("=-="*20)

# Mostra quantos números foram digitados
print(f"Foram digitados {len(numeros)} números.")

# Mostra uma lista ordenada de forma decrescente
print(f"A lista ordenada de forma decrescente {numeros_orde_reve}")

# Mostra quantas vezes o número 5 foi digitado, caso for nenhuma ele mostra que não foi digitado nenhuma vez
if numeros.count(5) >= 1:
    print(f"O número 5 faz parte da lista.")
else:
    print(f"O número 5 não faz parte da lista.")
