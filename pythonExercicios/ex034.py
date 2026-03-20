salario = float(input('Qual é o seu salário?: '))
if salario>1250: 
    print(f'O seu salário atualizado é de:{((salario/100)*10+salario):.2f}')
else:
    print(f'O seu salário atualizado é de:{((salario/100)*15+salario):.2f}')