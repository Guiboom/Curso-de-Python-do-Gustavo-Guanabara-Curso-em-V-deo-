def ficha(nome='<desconhecido>', gols=0):
    return(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome = input('Nome do jogador: ')
gols = int(input('Número de gol: '))

print(ficha(nome, gols))
print(ficha('Carlos', 33))
print(ficha(gols=33))
print(ficha('Carlos'))
print(ficha())