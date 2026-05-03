n1 = float(input('Digite o comprimento de uma reta:'))
n2 = float(input('Digite o comprimento de outra reta:'))
n3 = float(input('Digite o comprimento de outra reta:'))
if n1+n2>n3 and n1+n3>n2 and n2+n3>n1:
    print("Com esses comprimentos é posivel formar um triangulo!")
    if n1==n2 and n2==n3:
        print('O triangulo é Equilátero.')
    elif n1==n2 or n2==n3 or n3==n1:
        print('O triangulo é Isóceles.')
    else:
        print('O triangulo é Escaleno.')
else:
    print('Não é possivel formar um triangulo')
