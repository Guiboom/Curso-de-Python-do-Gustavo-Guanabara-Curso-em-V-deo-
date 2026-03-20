numerosExtensos = ("zero","um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
num=0
while True:
    num = int(input("Digite um número de 0-20: ")) 
    if num<0:
        print("Número invalido!")
    else:
        try:
            print(f"Você digitou o número {numerosExtensos[num]}.")
            break
        except:
            print("Número invalido!")
