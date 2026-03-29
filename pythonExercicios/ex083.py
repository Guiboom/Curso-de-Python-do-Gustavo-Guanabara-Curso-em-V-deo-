# Pede ao usuário para digitar uma expressão matemática
resposta = (input("Digite uma expressão matematica com parênteses: "))

# Cria uma lista que vai funcionar como uma "pilha" para controlar os parênteses
lista_carac = []

# Um laço criado para analisar cada caractere da resposta do usuário
for carac in resposta:
    
    # Se o caractere for um parêntese de abertura, ele é adicionado à lista
    if carac == '(':
        lista_carac.append('(')
    
    # Se o caractere for um parêntese de fechamento, o código checa se há um par para ele
    elif carac == ')':
        
        # Se a lista não estiver vazia, removemos o parêntese de abertura correspondente
        if len(lista_carac) > 0:
            lista_carac.pop()
        
        # Se a lista estiver vazia, significa que um parêntese fechou sem nunca ter sido aberto
        else:
            lista_carac.append(')') # Adiciona para indicar o erro
            # Interrompe o laço, pois a expressão já está errada
            break

# Se ao final de tudo a lista estiver vazia, todos os parênteses foram abertos e fechados corretamente
if len(lista_carac) == 0:
    print('Expressão correta!')

# Caso contrário, sobraram parênteses sem par
else:
    print("Expressão incorreta!")