import time

def maior(lst):
    """
    Analisa uma coleção de dados e identifica o maior valor numérico.
    Aceita tuplas, listas e dicionários.
    """
    # Verifica se a entrada é um dicionário e converte para lista de valores
    if type(lst) == dict:
        lst = list(lst.values())

    try:
        # Define o primeiro elemento como referência inicial
        nummaior = lst[0]
        
        print("=~=" * 15)
        print("(", end="")
        
        # Itera sobre a coleção para encontrar o maior valor
        for num in lst:
            if num > nummaior:
                nummaior = num
            
            # Efeito visual de processamento no terminal
            time.sleep(0.1)
            print(num, end=" ", flush=True)
            
        # Exibe o resumo da análise e o resultado final
        print(f") Foram informados {len(lst)} números.")
        print(f"O maior valor identificado foi: {nummaior}.")
        time.sleep(1)
        
    except IndexError:
        # Tratamento para coleções vazias
        print("\nErro: A coleção fornecida está vazia ou é inválida.")

# --- Bases de Dados para Teste ---

# Conjuntos do tipo Tupla (Imutáveis)
numeros = (1, 2, 3, 4, 5, 6, 7, 8)
numeros_com_zero = (0, 1, 2, 3, 4, 5)
so_zeros = (0, 0, 0, 0)
numeros_grandes = (1000, 500, 0, 250, 10000)
mistura_total = (-10, -5, 0, 5, 10)
decimais = (0.0, 0.5, 1.25, 3.14, 0.0)
zero_unitario = (0,)
nada = ()
esparsos = (0, 100, 200, 500, 1000)

# Conjuntos do tipo Lista (Mutáveis)
pontuacoes = [120, 450, 78, 900, 10, 540, 670]
temperaturas = [-5.5, -10.2, 0, -1.0, 4.5, -12.8, 2.0]

# Conjunto do tipo Dicionário (Chave: Valor)
notas_alunos = {
    "Marcos": 7.5, 
    "Julia": 9.2, 
    "Pedro": 6.0, 
    "Ana": 10.0, 
    "Lucas": 8.5
}

# --- Execução dos Testes ---

# Chamadas com Tuplas
maior(numeros)
maior(numeros_com_zero)

# Chamadas com Listas
maior(pontuacoes)
maior(temperaturas)

# Chamada com Dicionário (Conversão interna automática)
maior(notas_alunos)

# Teste de erro (Coleção vazia)
maior(nada)

#Obs: Código feito por min, a IA so organizou depois de pronto!