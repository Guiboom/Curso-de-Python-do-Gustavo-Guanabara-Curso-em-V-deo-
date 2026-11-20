from rich import print
from rich.panel import Panel
import time

class Livro:
    def __init__(self, titulo="", paginas=1):
        self.titulo = titulo
        self.paginas_contem = paginas
        self.pagina_atual = 1
        mensagem = f"Você acabou de abrir o livro '{self.titulo}' que tem {self.paginas_contem} páginas no total. Você agora está na página {self.pagina_atual}."
        print(Panel(mensagem, title="Leitura iniciada", border_style="green"))
    
    def avancar_paginas(self, paginas_avancar=1):
        
        if paginas_avancar <1:
            return "Por favor insira um valor maior que 0!" 
        
        if self.paginas_contem - self.pagina_atual == 0:
            return f"Já foi lido toda as {self.pagina_atual} paginas do livro!"
        
        if self.paginas_contem - self.pagina_atual >= paginas_avancar:
            for i in range(paginas_avancar):
                self.pagina_atual += 1
                print(f"Pag {self.pagina_atual}", end=" -> ")
                time.sleep(1)
            print()
            if self.pagina_atual != self.paginas_contem:
                return(f"Você avançou {paginas_avancar} paginas, e agora está na página {self.pagina_atual}")
            if self.pagina_atual == self.paginas_contem:
                return f"Você avançou {paginas_avancar} paginas, e agora o livro foi terminado!"
            
                
                
        else:            
            for i in range(paginas_avancar):
                self.pagina_atual += 1
                print(f"Pag {self.pagina_atual}", end=" -> ")
                time.sleep(1)
                if self.pagina_atual == self.paginas_contem:
                    break
            print()
            print(f"Você avançou somente {i+1} paginas, e agora o livro terminou!")
            if self.pagina_atual == self.paginas_contem:
                return f"O livro {self.titulo} terminou!"
        
                


p1 = Livro("O livro", 20)
print(p1.avancar_paginas(5))
print(p1.avancar_paginas(12))
print(p1.avancar_paginas(12))
        