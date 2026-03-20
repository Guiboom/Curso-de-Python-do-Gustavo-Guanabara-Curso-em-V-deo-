""" n1 = input('Digite um valor: ')
n2 = int(input('Digite um valor: '))
print("O tipo de variavel do 1° numero")
print(type(n1))
print("O tipo de variavel do 2° numero")
print(type(n2)) """

n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))
s = n3 + n4
#print('A soma entre ',n3,' e ',n4,' vale: ',s)
print('A soma entre {} e {} vale {}'.format(n3,n4,s))