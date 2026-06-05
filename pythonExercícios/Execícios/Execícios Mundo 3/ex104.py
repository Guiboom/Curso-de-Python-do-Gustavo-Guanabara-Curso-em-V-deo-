import sys
def leiaInt(n=0):
    """Função que funciona de forma semelhante à função input(), mas faz 
        a validação de tipo para aceitar APENAS números inteiros.
        
        O programa continuará em laço (loop) até que um valor inteiro válido seja digitado.
        
        :param msg: (Opcional) O texto que será exibido para o usuário no input.
        :return: Retorna o valor inteiro digitado e validado."""
    
    while True:
        try:
            n = int(input(n))
            return(n)
        except:
            print('\033[31mERRO! Digite um número inteiro válido.\033[0m')
        
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')