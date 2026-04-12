nomes_idades=list()
while True:
    nome = (input("Qual é o nome?: "))
    nota = int(input("Qual a 1ª nota?: "))
    nota2 = int(input("Qual a 2ª nota?: "))
    media = (nota + nota2)/2
    nomes_idades.append([nome,[nota,nota2],media])
    if input('Quer continuar?(S/N): ').upper().strip() == 'N':
        break

print("-=-"*30)

print('|No.   |NOME           |Média')

for i in range(len(nomes_idades)):
    print(f"|{i:<6}|{nomes_idades[i][0]:<15}|{nomes_idades[i][2]}")

print("-=-"*30)


while True:
    chc = str(input("Mostrar notas de qual aluno? se n quiser digite N: "))
    if chc.upper().strip() == 'N':
        break
    try:
        chc = int(chc)
        print(f"Notas de {nomes_idades[chc][0]} são {nomes_idades[chc][1]}")
    except:
        print("Digite o número de um aluno válido!")

print("=+-"*20)
print("PROGRAMA FINALIZADO!".center(60))
print("-+="*20)