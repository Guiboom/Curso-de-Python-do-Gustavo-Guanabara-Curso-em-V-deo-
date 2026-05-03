falha = 0
num = int(input('Digite um número para verificar se ele é primo: '))
for c in range(1,num+1):
    if num % c == 0:
        falha = falha + 1
    else:
         falha = falha
if falha>2 or num==1:
    print("O número não é primo")
else:
    print("O número é primo")