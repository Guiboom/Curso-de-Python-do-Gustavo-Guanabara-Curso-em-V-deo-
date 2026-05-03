lista_jogadores = list()
chc = 0
while True:
    try:
        InformaçõesJogador = dict()
        list_gols = list()
        total_gols = 0

        InformaçõesJogador["nome"] = input("Nome do jogador: ")
        InformaçõesJogador["partidas"] = int(
            input(f'Quantas partidas {InformaçõesJogador["nome"]} jogou?: ')
        )
        if InformaçõesJogador["partidas"] < 0:
            raise ValueError

        for i in range(InformaçõesJogador["partidas"]):
            gols = int(input(f"Quantos gols na partida {i+1}?: "))
            if gols < 0:
                raise ValueError
            list_gols.append(gols)
            total_gols += gols

        InformaçõesJogador["gols"] = list_gols[:]
        InformaçõesJogador["total_gols"] = total_gols

        lista_jogadores.append(InformaçõesJogador.copy()) #Adiciona todos os dicionario de cada jogadores a lista
        print('-=-'*30)
        if (input("Quer continuar? (S/N): ")).strip().upper() == "N":
            print('-=-'*30)
            print("Cod Nome           Gols           Total")
            for i in range(len(lista_jogadores)):
                print(f"{i:<4}{lista_jogadores[i]['nome']:<15}{str(lista_jogadores[i]['gols']):<15}{lista_jogadores[i]['total_gols']:<5}")
            while True:
                try:
                    chc = int(input('Mostrar dados de qual jogador (-1 para): '))
                    if 0 <= chc < len(lista_jogadores):
                        print("-=-"*20)
                        print(f"LEVANTAMENTO DO JOGADOR {lista_jogadores[chc]['nome']}")
                        for i in range(len(lista_jogadores[chc]['gols'])):
                            print(f"No jogo {i+1} ele fez {lista_jogadores[chc]['gols'][i]}")
                        print("-=-"*20)  
                    elif chc == -1:
                        break
                    else:
                        print("Jogador não encontrado!")
                except ValueError:
                    print("Error: Algo deu errado, tente novamente!")

        if chc == -1:
            break
                    
                
        print('-=-'*30)

    except:
        InformaçõesJogador.clear()
        print("Error: Algo deu errado, tente novamente!")
