from rich import print

class Caneta:
    def __init__(self, cor="azul"):
        # Atributo que define a cor da caneta (padrão é azul)
        self.cor = cor.lower()
        # Toda caneta começa tampada por segurança
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def tampar(self):
        self.tampada = True

    def escrever(self, texto):
        if self.tampada:
            print(f"[red]ERRO:[/] A caneta {self.cor} está tampada! Destampe antes de escrever.")
        else:
            # Mapeamento de cores em português para tags da biblioteca rich
            cores = {
                "azul": "blue",
                "vermelha": "red",
                "vermelho": "red",
                "verde": "green",
                "amarela": "yellow",
                "amarelo": "yellow",
                "roxa": "purple",
                "roxo": "purple"
            }
            cor_rich = cores.get(self.cor, "white")
            print(f"[{cor_rich}]{texto}[/]")

    def quebrar_linha(self, quantidade=1):
        print("\n" * (quantidade - 1))

# --- Exemplo de uso ---
c1 = Caneta("Azul")
c2 = Caneta("Vermelha")
c3 = Caneta("Verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, Pequeno Gafanhoto!")
c1.quebrar_linha(2)
c2.escrever("Aprendendo POO com Python.")
c3.escrever("Desafio 021 concluído!")

c1.tampar()
c1.escrever("Tentando escrever com a caneta tampada...")
