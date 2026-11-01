from rich import print
from rich.table import Table

tabela = Table(title="Tabela de preçoes")

tabela.add_column("Nome")
tabela.add_column("Preço")

tabela.add_row("Lápis", "[green]R$1,50[/]")
tabela.add_row("Borracha", "[green]R$4,50[/]")

print(tabela)