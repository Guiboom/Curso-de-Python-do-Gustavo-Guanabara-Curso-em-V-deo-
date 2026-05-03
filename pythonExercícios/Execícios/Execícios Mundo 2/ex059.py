from time import sleep
escolha = 0
num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
while escolha != 5:
    print("===============================")
    escolha = int(
        input(
            ""
            "(1)Somar\n"
            "(2)Multiplicar\n"
            "(3)Maior Valor\n"
            "(4)Digitar novos números\n"
            "(5)Sair do programa\n"
            "Selecione uma opção:"
        )
    )
    if escolha == 1:
        resultado = num1 + num2
        print(f"O resultado de {num1} + {num2} é:{resultado:.2f}")
    elif escolha == 2:
        resultado = num1 * num2
        print(f"O resultado de {num1} x {num2} é:{resultado:.2f}")
    elif escolha == 3:
        if num1 == num2:
            print("os números são iguais")
        elif num1 > num2:
            print(f"o número {num1} é o maior.")
        else:
            print(f"o número {num2} é o maior.")
    elif escolha == 4:
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite um número: "))
    elif escolha == 5:
        print(f"Programa finalizado!")
    else:
        print(f"Digite uma opção válida.")
    sleep(2)
