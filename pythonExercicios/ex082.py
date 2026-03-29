# Cria uma lsita
numeros = []
numeros_pares = []
numeros_impares = []


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

        # Senão ele transforma em inteiro e adiciona as suas respectivas listas
        else:
            resposta = int(resposta)
            numeros.append(resposta)
            if resposta % 2 == 0:
                numeros_pares.append(resposta)
            if resposta % 2 != 0:
                numeros_impares.append(resposta)

    # Lida com erros de usuário
    except:
        print("Digite um valor inteiro ou resposta válida!")

# Para deixar mais organizado
print("=-=" * 20)

# Mostra a lista normal
print(f"Lista de números: {numeros}")

# Mostra a lista de números pares
print(f"Lista de números pares: {numeros_pares}")

# Mostra a lista de números impares
print(f"Lista de números impares: {numeros_impares}")
