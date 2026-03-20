num = int(input('Digite um número inteiro: '))
escolha = input('Você deseja converter esse numero para:\n(1)Binario\n(2)octal\n(3)hexadecimal\n:')
escolha = escolha.strip()
if escolha == '1':
    print(f'O valor em binário fica em: {format(num, "b")}.')
elif escolha == '2':
    print(f'O valor em octal fica em: {oct(num)[2:]}.')
elif escolha == '3':
    print(f'O valor em hexadecimal fica em: {hex(num)[2:]}.')
else:
    print("Opção inválida, digite 1, 2 ou 3.")