from datetime import date

def voto(ano):
    """-> Verifica se pode, deve ou não pode votar.
        :param ano: ano de nascimento
        :return: NEGADO, OPCIONAL, OBRIGATÓRIO
        """
    ano_atual = date.today().year
    idade = ano_atual - ano

    if idade < 16:
        return 'NEGADO'
    
    elif idade < 18 or idade > 70 :
        return 'OPCIONAL'
    
    elif idade < 69:
        return 'OBRIGATÓRIO'
    
ano = int(input("Em que ano você nasceu?: "))
status = voto(ano)
print(f'Com base na sua idade, o seu voto é: {status}')