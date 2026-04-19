pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#print(pessoas['nome'])
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#print(pessoas.keys()) #= dict_keys(['nome', 'sexo', 'idade'])
#print(pessoas.values()) #=dict_values(['Gustavo', 'M', 22])
#print(pessoas.items()) #=dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])

#for k, v in pessoas.items():
#    print(f'{k} = {v}')
#nome = Gustavo
#sexo = M
#idade = 22

#del pessoas['sexo']
#for k, v in pessoas.items():
#    print(f'{k} = {v}')
#nome = Gustavo
#idade = 22 

#pessoas['nome'] = 'Leandro'
#for k, v in pessoas.items():
#    print(f'{k} = {v}')
#nome = Leandro
#sexo = M
#idade = 22

#brasil = []
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'São paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)

#print(estado1)
#print(brasil[1]) 
#print(brasil) #2 dicionário dentro de uma lista
#print(brasil[0]['sigla'])
#print(brasil[1]['sigla'])


estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # e tipo u=tilizar o [:] na lista
for e in brasil:
    for k, v in e.items():
        print(v, end=' ')
    print()