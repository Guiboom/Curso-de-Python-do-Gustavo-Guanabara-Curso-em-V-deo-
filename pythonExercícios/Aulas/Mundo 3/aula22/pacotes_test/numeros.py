from pacote import numeros

num = int(input("Digite um número: "))
fat = numeros.fatorial(num)
dob = numeros.dobro(num)
tri = numeros.triplo(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {dob}")
print(f"O triplo de {num} é {tri}")
