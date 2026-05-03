valor = float(input('Digite o valor do produto: '))
forma = int(input(
        'Qual a forma de pagamento:\n'
    '(1) À vista dinheiro/cheque (10% desconto)\n'
    '(2) À vista no cartão (5% desconto)\n'
    '(3) Em até 2x no cartão (sem juros)\n'
    '(4) Em até 3x no cartão (20% juros)\n'
    'Digite a opção: '
))
valorFinal = valor
if forma == 1:
    valorFinal = valor*0.9
    print(f'O preço ficará em R${valorFinal:.2f}')
elif forma == 2:
    valorFinal = valor*0.95
    print(f'O preço ficará em R${valorFinal:.2f}')
elif forma == 3:
    print(f'O preço total ficará em R${valorFinal:.2f}')
elif forma == 4:
    valorFinal = valor*1.20
    print(f'O preço total ficará em R${valorFinal:.2f}')
else:
    print('Digite uma opção valida.')