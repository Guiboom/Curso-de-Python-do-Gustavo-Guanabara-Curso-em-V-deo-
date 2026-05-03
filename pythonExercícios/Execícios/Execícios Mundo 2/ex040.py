nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
print(f'A média das notas é: {media}\n')
if media<5:
    print("Reprovado")
elif media>=5 and media<7:
    print('Recuperação')
else:
    print('Aprovado')