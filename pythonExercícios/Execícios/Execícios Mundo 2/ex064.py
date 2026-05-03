print('Para parar digite 999\n')
num=soma=cont=0
while num !=999:
    num = int(input('Digite números para somar: '))
    if num !=999:
        soma+=num
        cont+=1
print(f'Você digitou {cont} vezes, e a soma de todos os números é de {soma}')