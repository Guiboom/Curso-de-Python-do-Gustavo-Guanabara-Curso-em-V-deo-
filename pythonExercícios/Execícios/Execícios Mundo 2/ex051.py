primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(10):
    termo = primeiro + c * razao
    print(termo, end='-->')