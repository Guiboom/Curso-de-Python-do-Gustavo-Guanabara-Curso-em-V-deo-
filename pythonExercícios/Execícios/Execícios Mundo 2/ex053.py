frase = input('Digite uma frase: ')
frase = frase.replace(" ","").lower()
quantidade = len(frase)
letraFinal = -1
falhas=0
for c in range(0,quantidade):
    if frase[c] != frase[letraFinal]:
        falhas+=1
    letraFinal= letraFinal-1

if falhas>0:
    print('A frase não é um palíndromo')
else:
    print('A frase é um palíndromo')

