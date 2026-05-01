lista_jogadores = list()
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
        lista_jogadores.append(InformaçõesJogador.copy()) #Adiciona todos os dicionario de cada jogadores a lista
        print('-=-'*30)
        if (input("Quer continuar? (S/N): ")).strip().upper() == "N":
            print('-=-'*30)
            print("Cod Nome           Gols           Total")
            for i in range(len(lista_jogadores)):
                print(f"{i:<4}{lista_jogadores[i]['nome']:<15}{str(lista_jogadores[i]['gols']):<15}{total_gols:<5}")
            while True:
                try:
                    chc = int(input('Mostrar dados de qual jogador (-1 para): '))
                    if chc!= -1:
                        print(f"LEVANTAMENTO DO JOGADOR {lista_jogadores[chc]['nome']}")
                        for i in range(len(lista_jogadores[chc]['gols'])):
                            print(f'No jogo {i} ele fez {lista_jogadores[chc]["gols"]}')
                        
                    else:
                        break
                except ValueError:
                    print("Error: Algo deu errado, tente novamente!")
        print('-=-'*30)

    except:
        InformaçõesJogador.clear()
        print("Error: Algo deu errado, tente novamente!")

# ==============================================================================
# REVISÃO DE ERROS IDENTIFICADOS NO CÓDIGO:
# ==============================================================================

# 1. ERRO DO "TOTAL" NA TABELA:
# O código usava a variável 'total_gols' dentro do loop de exibição.
# Problema: Essa variável guardava apenas o valor do último jogador cadastrado.
# Correção: Salvar o total dentro do dicionário de cada jogador usando sum() 
# ou calcular a soma da lista específica durante a iteração.

# 2. EXIBIÇÃO DETALHADA (LISTA DE GOLS):
# No levantamento individual, o print chamava a lista completa: ["gols"].
# Problema: Isso imprimia a lista inteira em todas as linhas do loop.
# Correção: Acessar o índice específico da iteração: ["gols"][i].

# 3. LOGICA DO LOOP DE CONTINUAÇÃO:
# A tabela e a busca estavam dentro do loop principal de input.
# Problema: O programa tentava cadastrar um novo jogador após a busca e
# a limpeza do dicionário no 'except' poderia gerar erros de variável inexistente.
# Correção: Usar 'break' para encerrar o cadastro e mover a exibição/busca 
# para fora do loop principal.

# ==============================================================================