mais18 = homens = mulhermenos20 = 0

while True:

    while True:
        sexo = input("Digite o sexo(H/M): ").upper().strip()
        if sexo == "H" or sexo == "M":
            break

    while True:
        idade = input("Digite a idade: ")
        if idade.isdigit():
            idade = int(idade)
            if idade >= 0:
                break

    if idade > 18:
        mais18 += 1
    if sexo == "H":
        homens += 1
    if sexo == "M" and idade < 20:
        mulhermenos20 += 1

    chc = input("Quer continuar?(S/N): ")
    chc = chc.upper().strip()
    if chc == "N":
        break

print(f"\nResultados:")
print(f"- Pessoas com mais de 18 anos: {mais18}")
print(f"- Total de homens cadastrados: {homens}")
print(f"- Mulheres com menos de 20 anos: {mulhermenos20}")
