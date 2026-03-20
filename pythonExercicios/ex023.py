try:
    num = int(input("Digite um número entre 0-9999: "))
except ValueError:
    print("Erro: Você digitou letras ou caracter inválido.")
    exit()

if num <= 9999 and num >= 0:
    nums = str(num)
    nums = nums.zfill(4)
    print(f"Milhar {nums[0]}\nCentena {nums[1]}\nDezena {nums[2]}\nUnidade {nums[3]}")
else:
    print("Erro: Você digitou um caracter ou quantidade inválida.")