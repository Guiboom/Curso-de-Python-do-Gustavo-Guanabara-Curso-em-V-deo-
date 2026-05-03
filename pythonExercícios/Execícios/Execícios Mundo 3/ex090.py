aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input('Média: '))

print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')

if aluno['media']>=6:
    aluno['situação'] = 'Aprovado'
    print("Situação é igual a Aprovado")
else:
    aluno['situação'] ='Reprovado'
    print("Situação é igual a Reprovado")