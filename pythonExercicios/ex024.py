nomeCidade = input('Digite o nome de uma cidade: ')
nomeCidade = nomeCidade.upper().strip()
if nomeCidade.startswith('SANTO'):
    print('A cidade começa com o nome santo')
else:
    print('A cidade não começa com a palavra santo')