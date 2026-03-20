nome = input('Digite o seu nome: ')
print('Maiuscula:')
print(nome.upper())

print('\nMinuscula:')
print(nome.lower())

print('\nQuantas letras tem sem contar os espaços:')
print(len(nome.replace(' ', '')))

print('\nQuantas letras tem o primeiro nome:')
primeiroNome = nome.split()[0]
tamanho1Nome= len(primeiroNome)
print(tamanho1Nome)