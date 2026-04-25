pessoas_lista = list()
soma_idade = 0

while True:

    pessoa = {
        'nome' : input("Nome: "),
        'sexo' : (input("Sexo (M/F): ")).upper().strip(),
        'idade' : int(input("Idade: ")),
    }
    pessoas_lista.append(pessoa)
    
    if (input('Quer continuar? (S/N): ')).strip().upper() == 'N':
        break

for pessoa in pessoas_lista:
    soma_idade += pessoa['idade']
media_idade = soma_idade / len(pessoas_lista)

print('=-='*20)

print(f'Total de pessoas cadastradas: {len(pessoas_lista)}')  
print(f'Média de idade das pessoas cadastradas: {media_idade:.2f} anos')  

print('Nome das mulheres cadastradas: ',end='')
for pessoa in pessoas_lista:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'],end=' ')
        
print('\nLista de pessoas que estão com a idade acima da média: ',end='')
for pessoa in pessoas_lista:
    if pessoa['idade'] > media_idade :
        print(pessoa['nome'])

