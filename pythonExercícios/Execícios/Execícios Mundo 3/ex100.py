import random
numeros = []

def sorteia(lst):
    print("Sorteando 5 valores da lista:", end='')
    for i in range(5):
        lst.append(random.randint(1,100))
        print(lst[-1], end=' ')
    print()

    
def somaPar(lst):
    somaPares= 0
    print("Somando os valores pares de:", end='')
    for num in lst:
        if num % 2 == 0:
            somaPares += num
    print(lst, end='')
    print(f"temos {somaPares}")
              
sorteia(numeros)
somaPar(numeros)