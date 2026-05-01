while True:
    try: 
        Informações= dict()
        list_gols = list()
        total_gols=0

        Informações['nome'] = input("Nome do jogador: ")
        Informações['partidas'] = int(input(f'Quantas partidas {Informações["nome"]} jogou?: '))
        if Informações['partidas'] < 0:
            raise ValueError

        for i in range(Informações['partidas']):
            gols = int(input(f"Quantos gols na partida {i+1}?: "))
            if gols < 0:
                raise ValueError
            list_gols.append(gols)
            total_gols += gols

        Informações['gols'] = list_gols
        Informações['total de gols'] = total_gols

        print("=-="*20)
        print(Informações)
        print("=-="*20)

        print(f'Nome: {Informações["nome"]}')
        print(f'Gols por partida: {Informações["gols"]}')
        print(f'Total de gols: {Informações["total de gols"]}')

        print("=-="*20)

        print(f"O jogador {Informações['nome']} jogou {Informações['partidas']} partidas")
        for i in range(Informações['partidas']):
              print(f"  ==> Na partida {i+1}, fez {Informações['gols'][i]} gols.")
        print(f'Foi um total de {Informações['total de gols']} gols.')

        break
    except:
        print("Error: Algo deu errado, tente novamente!")