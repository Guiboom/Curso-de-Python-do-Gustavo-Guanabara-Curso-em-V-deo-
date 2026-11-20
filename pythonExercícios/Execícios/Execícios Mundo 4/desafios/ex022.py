from rich import print
from rich.panel import Panel

class ControleRemoto:
    # Atributos de classe (configuração padrão)
    canal_minimo = 1
    canal_maximo = 5
    volume_minimo = 1
    volume_maximo = 5

    def __init__(self, canal_atual=1, volume_atual=2):
        # Atributos de instância
        self.canal_atual = canal_atual
        self.volume_atual = volume_atual
        self.ligado = False

    def liga_desliga(self):
        # Alterna entre ligado e desligado
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_maximo:
                self.canal_atual = ControleRemoto.canal_minimo
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_minimo:
                self.canal_atual = ControleRemoto.canal_maximo
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_maximo:
                self.volume_atual += 1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_minimo:
                self.volume_atual -= 1

    def mostrar_tv(self):
        if not self.ligado:
            conteudo = "[red]:no_entry: A TV está desligada[/red]"
        else:
            # Montando a linha de canais
            canais_str = ""
            for canal in range(ControleRemoto.canal_minimo, ControleRemoto.canal_maximo + 1):
                if canal == self.canal_atual:
                    canais_str += f"[black on yellow] {canal} [/black on yellow]"
                else:
                    canais_str += f" {canal} "

            # Montando a barra de volume
            volume_str = ""
            for vol in range(ControleRemoto.volume_minimo, ControleRemoto.volume_maximo + 1):
                if vol <= self.volume_atual:
                    volume_str += "[black on cyan] [/black on cyan]"
                else:
                    volume_str += "[black on white] [/black on white]"

            conteudo = f"Canal:  {canais_str}\nVolume: {volume_str}"

        print(Panel(conteudo, title="[yellow]TV[/yellow]", width=30))


# --- Bloco Principal / Teste com Loop Interativo ---
if __name__ == "__main__":
    tv = ControleRemoto()

    while True:
        tv.mostrar_tv()
        
        comando = input("Comandos ([@] Ligar/Desligar | [<][>] Canais | [-][+] Volume | [0] Sair): ")
        
        if comando == "0":
            break
        elif comando == "@":
            tv.liga_desliga()
        elif comando == ">":
            tv.canal_mais()
        elif comando == "<":
            tv.canal_menos()
        elif comando == "+":
            tv.volume_mais()
        elif comando == "-":
            tv.volume_menos()
            
        print("\n" * 10)