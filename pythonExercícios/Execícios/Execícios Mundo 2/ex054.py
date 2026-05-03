from datetime import date
anoAtual = date.today().year
maiores=0
menores=0
for c in range(7):
    aniversario = int(input(f'Digite o ano de nascimento da {c+1}ª pessoa:'))  
    if anoAtual - aniversario>21: #ele pediu para ser 21
        maiores+=1
    else:
        menores+=1
print(f'Desses listados,{maiores} são maiores de idade e {menores} são menores')