from rich import print
from rich.panel import Panel

class Livro:
    def __init__(self, titulo="", paginas=1):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        mensagem = f"Você acabou de abrir o livro '{self.titulo}' que tem {self.paginas} páginas no total. Você agora está na página 1."
        print(Panel(mensagem, title="Leitura iniciada", border_style="green"))
    
    def avancar_paginas(self, paginas_avancar=1):
        while self.paginas - self.pagina_atual <= paginas_avancar:
            for i in range(paginas_avancar):
                return(f"Pag{i}")
                
p1 = Livro("O livro", 20)
p1.avancar_paginas(5)
        