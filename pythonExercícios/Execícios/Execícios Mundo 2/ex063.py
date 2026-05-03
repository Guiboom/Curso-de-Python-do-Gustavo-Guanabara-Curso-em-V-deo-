num = int(input("Digite a quantidade de números da sequência de Fibonacci que devem aparecer: "))
n1 = 0
n2 = 1
cont = 0
if num <= 0:
    print("Por favor, entre com um número positivo.")
elif num == 1:
    print(n1)
else:
    print("Sequencia Fibonacci: ")
    while cont < num:
        print(n1,"->",end=" ")
        proximo = n1 + n2
        n1 = n2
        n2 = proximo
        cont += 1
print("Fim",end=' ')
