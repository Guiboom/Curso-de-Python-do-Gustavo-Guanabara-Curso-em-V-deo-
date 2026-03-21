# Declara um onjeto e uma variável
tupla_precos = (
    "Mouse pad",
    30,
    "Mouse USB",
    50,
    "Teclado mecânico",
    85,
    "Pen Drive 128gb",
    110,
    "SSD interno 480GB",
    250,
    "Memória RAM 8GB DDR4",
    300,
    "Gabinete",
    350,
    "Fonte de alimentação 600W",
    450,
    "Processador Ryzen 5 5500",
    600,
    "Placa de vídeo RX7600",
    1700,
)
titulo = "LISTAGEM DE PREÇOS"

# Cria um título
print("-=" * 21)
print(f"{titulo:^42}")
print("=-" * 21)

# Imprime o valor i da tupla até não haver mais, depois imprime uma linha de "=" e para.
for i in range(0, len(tupla_precos), 2):
    print(f"|{tupla_precos[i]:.<30}R$ {tupla_precos[i+1]:>7.2f}|")
print("=" * 42)
