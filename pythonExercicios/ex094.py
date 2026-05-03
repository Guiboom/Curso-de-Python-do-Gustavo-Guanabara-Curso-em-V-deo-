pessoas_lista = list()
soma_idade = 0

while True:

    pessoa = {}
    while True:
        try:
            pessoa["nome"] = input("Nome: ").strip()
            if pessoa["nome"] != "":
                break
            print("Digite um nome!")
        except:
            print("Digite um nome!")

    while True:
        try:
            pessoa["sexo"] = (input("Sexo (M/F): ")).upper().strip()
            if pessoa["sexo"] == "M" or pessoa["sexo"] == "F":
                break
            print("Digite um genero 'M' ou 'F'")
        except:
            print("Digite um genero 'M' ou 'F'")

    while True:
        try:
            pessoa["idade"] = int(input("Idade: "))
            if pessoa["idade"] > 0:
                break
            print("Digite a idade!")
        except:
            print("Digite a idade!")

    pessoas_lista.append(pessoa)

    if (input("Quer continuar? (S/N): ")).strip().upper() == "N":
        break

for pessoa in pessoas_lista:
    soma_idade += pessoa["idade"]
media_idade = soma_idade / len(pessoas_lista)

print("=-=" * 20)

print(f"Total de pessoas cadastradas: {len(pessoas_lista)}")
print(f"Média de idade das pessoas cadastradas: {media_idade:.2f} anos")

print("Nome das mulheres cadastradas: ", end="")
for pessoa in pessoas_lista:
    if pessoa["sexo"] == "F":
        print(pessoa["nome"], end=" ")

print("\nLista de pessoas que estão com a idade acima da média: ")
for pessoa in pessoas_lista:
    if pessoa["idade"] > media_idade:
        print(f"    Nome = {pessoa['nome']};", end=" ")
        print(f"    Sexo = {pessoa['sexo']};", end=" ")
        print(
            f"    Idade = {pessoa['idade']};",
        )
