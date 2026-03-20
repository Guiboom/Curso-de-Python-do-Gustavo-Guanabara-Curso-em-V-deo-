primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
vezes=0
while vezes <10:
    termo = primeiro + vezes * razao
    print(termo, end='-->')
    vezes+=1
print('Fim')