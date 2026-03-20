import random
alu1 = input('Digite o nome do 1° aluno: ')
alu2 = input('Digite o nome do 2° aluno: ')
alu3 = input('Digite o nome do 3° aluno: ')
alu4 = input('Digite o nome do 4° aluno: ')
lista = [alu1,alu2,alu3,alu4]
random.shuffle(lista)
print(f'A ordem de aluno escolhido foi: {lista}')