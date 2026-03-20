primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
razaoFix=razao
vezes=0

while vezes <10:
    termo = primeiro + vezes * razao
    print(termo, end='-->')
    vezes+=1

alem=1
while alem!=0:
    alem =  int(input('\nAlém desses, você deseja mais quantos termos? caso não queira digite(0): '))
    if alem !=0:
        alem += vezes 
    while vezes <alem:
        termo = primeiro + vezes * razao
        print(termo, end='-->')
        vezes+=1

print('Fim')