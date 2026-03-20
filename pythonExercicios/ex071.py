v50=v20=v10=v1=0

print("CAIXA ELETRÔNICO")

valor = int(input('Digite quantos Reais você quer sacar: '))
print(f'Para {valor}R$, aqui está:')

while True:
    
    if valor>=50:
        valor-=50
        v50+=1

    elif valor>=20:
        valor-=20
        v20+=1

    elif valor>=10:
        valor-=10
        v10+=1

    elif valor>=1:
        valor-=1
        v1+=1

    else: 
        if v50>0:
            print(f'{v50} cédulas de R$50')
        
        if v20>0:
            print(f'{v20} cédulas de R$20')
        
        if v10>0:
            print(f'{v10} cédulas de R$10')
        
        if v1>0:
            print(f'{v1} cédulas de R$1')   

        break
    