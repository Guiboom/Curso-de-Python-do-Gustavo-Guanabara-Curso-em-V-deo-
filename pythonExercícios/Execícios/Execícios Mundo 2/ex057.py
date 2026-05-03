sexo = input('Digite o seu sexo(M/F): ').upper()
while sexo !="M" and sexo !="F":
    sexo = input('Opção incorreta, Digite um valor válido(M/F): ').strip().upper()
print(f'Sexo {sexo} registrado.')