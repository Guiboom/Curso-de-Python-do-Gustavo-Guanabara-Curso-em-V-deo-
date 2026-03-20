n=0
while True:
    n = int(input('Digite um número(negativo para parar): '))
    if n<0:
        break
    cont=1
    print('-'*45)
    while cont < 11 :
        print(f'{n} x {cont} = {n*cont}')
        cont+=1
    print('-'*45)
print("Tabuada encerrada!")