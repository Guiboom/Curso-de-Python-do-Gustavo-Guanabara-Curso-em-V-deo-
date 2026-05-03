print('\033[0;33;41mOlá mundo!\033[m')
print('\033[0;32;43mOlá mundo!\033[m')
print('\033[0;31;42mOlá mundo!\033[m')
a=1
b=2
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
nome = 'Gustavo'
print(f'Olá! Muito prazer em te conhecer, {'\033[4;34m'}{nome}{'\033[m'}!!!')
cores = {'limpa':'\033 [m',
        'azul':'\033 [34m',
        'amarelo':'\033 [33m',
        'pretoebranco':'\033 [7;30m'}