#Cria uma lsita
numeros = []

#Avisa ao usuário como parar o código
print('Para parar digite "pare"!')

#Um laço criado para adicionar numeros não adicionados ainda à lista até que ele digite 'pare' ou 'PARE'
while True:
    
    #Pede ao usuário digitar um número
    resposta = input("Digite um número: ")
    
    try: 
        #Se o usuário digitar 'pare' ou 'PARE' ele para :)
        if resposta.upper().strip() == "PARE":
            break
        
        #Senão ele verifica se já foi adicionado, caso não, ele adiciona :)
        else:
            resposta = float(resposta)        
            if resposta in numeros:
                print("Valor já adicionado anteriormente!")
            else:
                numeros.append(resposta)
                print(f"Número {resposta} adicionado")

    #Lida com valores que não são experados, diferentes de números, 'pare' e 'PARE'
    except:
        print('Valor invalido, digite um número ou "pare" para parar o programa!')

#Para ficar mais organizado
print('=-='*30)

#Mostra os números digitados em ordem crescente
print(f'Aqui está os números digitados em ordem crescente: {sorted(numeros)}')