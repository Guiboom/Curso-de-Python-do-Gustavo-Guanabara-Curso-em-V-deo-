""" 
lanche = () tupla
lanche = [] lista
lanche = {} dicionario 
"""

# lanche = 'Hamburguer','Suco','Pizza','Pudim' é igual a do parenteses a tupla 

lanche = ('Hamburguer','Suco','Pizza','Pudim','Batata Frita')

#Tuplas são imutaveis
# lanche[1] = 'Refrigerante' não funciona!!!

""" print(lanche)  # 'Hamburguer','Suco','Pizza','Pudim' 
print(lanche[1]) # Suco 
print(lanche[-2]) # Pizza 
print(lanche[1:3]) # 'Suco','Pizza' 
print(lanche[:2]) # 'Hamburguer','Suco' 
print(lanche[-2:]) # 'Pizza', 'Pudim'  """

""" for comida in lanche:
    print(f'Eu vou comer {comida}')
print("Comi pra caramba!") """

#===São iguais o de cima e de baixo===

""" for cont in range(0, len(lanche)): #cont começa do 0 até a quantidade de elementos, dando print em cada dps
    print(f'Eu vou comer {lanche[cont]}')
print("Comi pra caramba!")  """

#print(len(lanche))

""" for cont in range(0, len(lanche)): #cont começa do 0 até a quantidade de elementos, dando print em cada dps
    print(lanche[cont]) """

""" for cont in range(0, len(lanche)): #cont começa do 0 até a quantidade de elementos, dando print em cada dps
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print("="*40)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}') """

""" print(sorted(lanche)) #ordenado """

""" a=(2,5,4)
b=(5,8,1,2)
c=b+a #5,8,1,2,2,5,4
d=a+b #2,5,4,5,8,1,2
print(c)
print(d)
print(c.count(5))
print(c.count(5,1))
print(c.count(9))
print(c.index(8)) """

pessoa = ('Gustavo', 39, "M", 99.88) #No python pode-se ter diferentes tipos de elementos nas tuplas
print(pessoa)
del(pessoa)