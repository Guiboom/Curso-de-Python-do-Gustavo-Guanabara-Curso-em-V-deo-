# Declara um objeto e uma variável
numerosExtensos = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "catorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)
num = 0

print('-='*22)
# O loop serve para testar infinitamente até que o usuário digite um valor correto (0-20)
while True:
    num = input("Digite um número de 0-20: ")

    # Testa se a string pode virar um valor inteiro e positivo
    if num.isdigit():

        # Transforma em inteiro
        num = int(num)

        # Testa se é um número de 0-20
        if 0 <= num <= 20:
            print(f"Você digitou o número {numerosExtensos[num]}.")
            print('-='*22)
            while True:
                chc = input('Você deseja digitar mais números?(S/N)').upper().strip()
                if chc == 'S' or chc == 'N':
                    print('Ok!')
                    print('-='*22)
                    break
                else:
                    print('Digite uma opção válida (S/N)!')

            if chc == 'N':
                break
        else:
            print("Digite um número inteiro válido!")
    else:
        print("Digite um número inteiro válido!")
print('Programa finalizado!')
