nome = input('Digite o seu nome: ')
nome = nome.upper().strip()
vezes = nome.count('A')
primeiraVez = nome.find('A')+ 1# soma 1 para não ficar 0 em nomes como "ana"
ultimaVez = nome.rfind('A')+1
if vezes > 0:
    print(f'A letra "A" aparece {vezes} vezes no seu nome')
    print(f'A letra "A" aparece pela primeira vez na posição {primeiraVez}')
    print(f'A letra "A" aparece pela ultima vez na posição {ultimaVez}')
else:
    print('O seu nome não aparece a letra "A" nenhuma vez :(')