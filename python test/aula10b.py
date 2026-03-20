n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1+n2)/2
print(f'A suas média foi:{m}')
if m > 10 or m<0:
    print('Digite um valor valido')
elif m >6:
    print('Sua media foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude mais!')