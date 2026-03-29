#Cria uma lista
numeros = []

#Esse laço rodará até que o laço tenha 5 valores númericos inteiros
while len(numeros) < 5:
    num = input('Digite um número: ')
    
    try:
        #Tenta converter para número inteiro
        num = int(num)
        
        #Se a lista estiver vazia ou se o número digitado for maior que todos da lista ele adiciona à ela em ultimo lugar
        if len(numeros) == 0 or num > numeros[-1]:
            numeros.append(num)
            
        #Senão ele vai passando em cada valor na lista até achar um valor menor ou igual e insere ele no mesmo lugar 
        else:
            for i in range(len(numeros)):
                if numeros[i] >= num:
                    numeros.insert(i,num)
                    break
    #Avisa ao usuário que o número que ele digitou não é um número inteiro
    except:
        print("Digite um número inteiro!")

#Para deixar mais organizado
print('=-='*30)

#Ele mostra os números digitados em forma númerica
print(f'Lista dos números digitados em forma númerica: {numeros}')