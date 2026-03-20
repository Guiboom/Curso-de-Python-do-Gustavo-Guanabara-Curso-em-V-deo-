from datetime import date
nascimento = int(input('Digite o ano que voce nasceu: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
print(f'Quem nasceu em {nascimento} tem ou terá {idade} em {ano_atual}')
if idade<18:
    tempoFalta = 18-idade
    print(f'Você terá que se alistar no exercito daqui a {int(tempoFalta)} anos.')
elif idade==18:
    print(f'Já está na hora de você se alistar no exercito.')
else:
    tempoFalta = idade-18
    print(f'Já passou {tempoFalta} do alistamento.')