n1 = float(input('Digite o comprimento de uma reta:'))
n2 = float(input('Digite o comprimento de outra reta:'))
n3 = float(input('Digite o comprimento de outra reta:'))
if n1+n2>n3 and n1+n3>n2 and n2+n3>n1:
    print("Com esses comprimentos é posivel formar um triangulo!")
else:
    print('Não é possivel formar um triangulo')