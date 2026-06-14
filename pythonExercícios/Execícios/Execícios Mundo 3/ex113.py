import sys
def leiaInt(n=0):
    """Função que funciona de forma semelhante à função input(), mas faz 
        a validação de tipo para aceitar APENAS números inteiros.
        
        O programa continuará em laço (loop) até que um valor inteiro válido seja digitado.
        
        :return: Retorna o valor inteiro digitado e validado."""
    
    while True:
        try:
            n = int(input(n))
            return(n)
        except:
            print('\033[31mERRO! Digite um número inteiro válido.\033[0m')

def leiafloat(n=0):
    """Função que funciona de forma semelhante à função input(), mas faz 
        a validação de tipo para aceitar APENAS números reais.
        
        O programa continuará em laço (loop) até que um valor real válido seja digitado.
        
        :return: Retorna o valor real digitado e validado."""
    
    while True:
        try:
            n = float(input(n))
            return(n)
        except:
            print('\033[31mERRO! Digite um número real válido.\033[0m')
        
n = leiaInt('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {n}, e o numero real {n2}')