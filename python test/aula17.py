# num = (2,5,9,1)#tupla
# num[2]= 3 não funciona pq é uma tupla
# print(num)

num = [2, 5, 9, 1]  # lista
# num[2]= 3 #funciona pq é uma lista
# num[4]=3 não funciona essa forma de adicionar numeros a lista
# num.append(7)#essa maneira é a correta
# num.sort()#poê em ordem
# num.sort(reverse=True)#poê em ordem inversa
# num.insert(2,0)#na posição 2 ele poê o 0, e os que estavam afrente da posição 1 vão pra frente
# num.pop()#remove o valor 1(ultima posição)
# num.pop(2)#remove o valor 0(posição 2)
num.insert(2,2)
num.remove(2)#remove apenas o 1º número 2
#num.remove(4)#dá erro se não houver na lista
if 4 in num:
    num.remove(4)
#else:
#    print("Não achei o 4")
#print(num)
#print(f'Essa lista tem {len(num)} elementos.')

#valores = []
#for cont in range(0,5):
#    valores.append(int(input('Digite um valor: ')))

#for c, v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}!')
#print('Final da lista')


a= [2,3,4,5]
b=a
b[2] = 8 #ele altera as duas listas
print(f'Lista A: {a}')
print(f'Lista B: {b}')


a= [2,3,4,5]
b=a[:] #ele cria uma cópia
b[2] = 8 
print(f'Lista A: {a}')
print(f'Lista B: {b}')

