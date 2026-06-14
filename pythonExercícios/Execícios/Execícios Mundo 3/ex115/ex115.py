import json
import time
import os

pessoas = list()

try:
    with open("pessoas.json", "r") as file:
        pessoas = json.load(file)
    print("pessoas carregadas!")

except FileNotFoundError:
    pessoas = []
    print("Arquivo não encontrado. Uma nova lista será criada ao sair.")
    

except json.JSONDecodeError:
    pessoas = []
    print("O arquivo de salvamento estava vazio ou corrompido. Iniciando nova lista.")

except Exception as e:
    pessoas = []
    print(f"Ocorreu um erro inesperado: {e}")

while True:
    try:
        print("-"*40)
        print('MENU PRINCIPAL'.center(40))
        print("-"*40)
        print('1- Ver pessoas cadastradas')
        print('2- Cadastrar nova pessoa')
        print('3- Sair do Sistema')
        print("-"*40)
        chc = int(input('Sua opção: '))
        
        if chc == 1:
            print("="*40)
            print(f'NOME',' '*26,'IDADE')
            print("="*40)
            for pessoa, idade in pessoas:
                print(f"{pessoa:<32}{idade} ANOS")
            print("="*40)
            
            
        elif chc == 2:
            pessoa = input('Digite o nome da pessoas: ')
            while True:
                try:
                    idade = int(input('Digite a idade da pessoas: '))
                    break
                except:
                    print("digite um valor inteiro valido!")
            pessoas.append([pessoa,idade])
            del pessoa, idade

        
        elif chc == 3: 
            with open("pessoas.json", "w") as file:
                json.dump(pessoas, file)
            print('Saindo.', end='', flush=True)
            time.sleep(1)
            print('.', end='', flush=True)
            time.sleep(1)
            print('.')
            time.sleep(1)
            break
        
        else:
            print("Escolha uma opção valida!")

    except ValueError:
        print("Escolha uma opção válida (1, 2 ou 3)!")
        


