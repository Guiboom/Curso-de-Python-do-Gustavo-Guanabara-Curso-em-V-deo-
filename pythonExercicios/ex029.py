velocidade = int(input("Digite a velocidade que vocè esta dirigindo em Km/h: "))
if velocidade> 80:
    multa = (velocidade-80)*7
    print(f'Você foi multado em {multa}R$!')
else:
    print('Parabéns Boa viajem!')