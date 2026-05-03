idadeMedia=0
idadeMaior=0
mulherMenosDe20=0
nomeHomenMaisVelho = "Nenhum nome de homen citado."
for c in range(4):
    nome= input(f'Digite o nome da {c+1}ª pessoa: ')
    idade = int(input(f'Digite a idade da {c+1}ª pessoa: '))
    sexo = int(input(f'Digite o sexo da {c+1}ª pessoa (1)Homen (2)Mulher: '))
    idadeMedia += idade
    if idade > idadeMaior and sexo==1:
        idadeMaior = idade
        nomeHomenMaisVelho = nome
    if sexo == 2 and idade<20:
        mulherMenosDe20+=1

idadeMedia= idadeMedia/4
print(f'A idade média do grupo é de:{idadeMedia} anos.')
print(f'O nome do homen mais velho é: {nomeHomenMaisVelho}.')
print(f'E dessas pessoas, {mulherMenosDe20} são mulheres com menos de 20 anos.')