from datetime import date
ano_atual = date.today().year

while True:
    try:
        cadastro = dict()

        print("=---Cadastro---=")
        cadastro['nome'] = input('Nome: ').strip()
        cadastro['idade'] = ano_atual - int(input('Ano de nascimento: '))
        cadastro['ctps'] = int(input('Número da carteira de trabalho (0 caso não tenha): '))

        if cadastro['ctps'] != 0:
            cadastro['contratação'] = int(input('Ano de contratação: '))
            cadastro['idade para aposentadoria'] = cadastro['idade'] + 35 - (ano_atual - cadastro['contratação'])
            cadastro['salário'] = float(input('Salário: '))

        #35 anos de colaboração

        print("=-="*20)

        print(f'Nome: {cadastro["nome"]}')
        print(f'Idade: {cadastro["idade"]}')
        print(f'ctps: {cadastro["ctps"]}')

        if cadastro['ctps'] != 0 :
            print(f'Ano de contratação: {cadastro["contratação"]}')
            print(f'Salário: {cadastro["salário"]:.2f}')
            if cadastro['idade para aposentadoria'] > 0:
                print(f'Status: Você deve se aposentar aos {cadastro["idade para aposentadoria"]} anos')
            else:
                print('Status: Você deve ou deveria estar aposentado!')

        print("=-="*20)   
        break
    except:
        print("Algo deu errado, tente novamente!")