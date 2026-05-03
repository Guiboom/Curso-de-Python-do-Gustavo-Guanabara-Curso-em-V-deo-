num = int(input('Digite números para somar: '))
chs='S'
vezes=1
maior=menor=soma=num
while chs =='S':
    num = int(input('Digite números para somar: '))
    soma+=num
    if num>maior:
        maior = num
    if num<menor:
        menor = num
    chs= input("Você quer continuar a digitar valores?(S/N): ").upper()
    vezes+=1
media=soma/vezes
print(f'A média de todos os números é {media:.3f}, o maior número é {maior}, e o menor número é {menor}.')