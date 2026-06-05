import pydoc
import time

def pyHelp():
    AZUL_VERMELHO = '\033[0;31;44m'
    VERDE_PRETO = '\033[0;30;42m'
    VERMELHO_PADRAO = '\033[0;31m'
    AMARELO_PADRAO = '\033[30;43m'
    ROXO_BRANCO = '\033[0;30;45m'
    C_FIM = '\033[m'
    LIMPAR = '\033[2J\033[H' 

    text01 = 'SISTEMA DE AJUDA PyHELP'
    tam_tit = len(text01) + 4

    while True:
        print(LIMPAR, end="")
        print(f"{AZUL_VERMELHO}{'~' * tam_tit}{C_FIM}")
        print(f"{AZUL_VERMELHO}  {text01}  {C_FIM}")
        print(f"{AZUL_VERMELHO}{'~' * tam_tit}{C_FIM}") 

        try:
            chc = input('Função ou Biblioteca: ')
            
            if not chc.strip():
                continue

            if chc.upper() == 'FIM':
                text_fim = 'ATÉ LOGO'
                tam_fim = len(text_fim) + 4
                print(f"{ROXO_BRANCO}{'~' * tam_fim}{C_FIM}")
                print(f"{ROXO_BRANCO}  {text_fim}  {C_FIM}")
                print(f"{ROXO_BRANCO}{'~' * tam_fim}{C_FIM}")
                break
            
            text_acesso = f'Acessando o manual do comando "{chc}"'
            tam_acesso = len(text_acesso) + 4
            print(f"{VERDE_PRETO}{'~' * tam_acesso}{C_FIM}")
            print(f"{VERDE_PRETO}  {text_acesso}  {C_FIM}")
            print(f"{VERDE_PRETO}{'~' * tam_acesso}{C_FIM}")
            
            time.sleep(1.5)
            
            texto_ajuda = pydoc.render_doc(chc, "Help on %s")
            
            print(LIMPAR + AMARELO_PADRAO, end="")
            print(texto_ajuda)
            
            input(f"\n{AMARELO_PADRAO}Pressione [ENTER] para voltar ao PyHelp...{C_FIM}")
            
        except Exception:
            print(f'{VERMELHO_PADRAO}Digite uma Função ou Biblioteca válida!!!{C_FIM}')
            time.sleep(1.5)
        
pyHelp()