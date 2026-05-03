"""teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste) #se alterar a lista teste altera dentro da lista galera tmb
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) # #se alterar a lista teste não altera dentro da lista galera pois é uma copia
print(galera)
"""

""" galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
print(galera) #[["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
print(galera[0]) #["João", 19]
print(galera[0][0]) #João
 """

""" galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
for p in (galera):
    print(p)
    print(p[0])
    print(p[1]) """

""" galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
for p in (galera):
    print(f'{p[0]} tem {p[1]} anos de idade') """   

""" galera = list()
dado = list()
for c in range(0,3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera) """

galera = list()
dado = list()
totmai = totmen = 0

for c in range(0,3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >20:
        print(f"{p[0]} é maior de idade")
        totmai+=1
    else:
        print(f"{p[0]} é menor de idade")
        totmen+=1
print(f"Temos {totmai} maiores e {totmen} menores de idade")
    