dist = float(input('Digite a distancia da viagem em Km: '))
if dist<=200:
    print(f'O preço por essa viagem é de {(dist*0.50):.2f}R$')
else:
    print(f'O preço por essa viagem é de {(dist*0.45):.2f}R$')