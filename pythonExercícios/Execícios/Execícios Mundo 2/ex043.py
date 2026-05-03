peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em Metros: '))
imc = peso/(altura**2)
if imc<18.5:
    print('Abaixo do peso:')
elif imc<25:
    print('Peso ideal.')
elif imc<31:
    print('Sobrepeso.')
elif imc<41:
    print('Obesidade.')
else:
    print('Obesidade Mórbida.')