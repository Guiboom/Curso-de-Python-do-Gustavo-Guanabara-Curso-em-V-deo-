n=soma=cont=0
while True:
    n = float(input('Digite um número (999 para parar): '))
    if n==999:
        break
    soma+=n
    cont+=1
print(f'soma={soma}  quantidade={cont}')