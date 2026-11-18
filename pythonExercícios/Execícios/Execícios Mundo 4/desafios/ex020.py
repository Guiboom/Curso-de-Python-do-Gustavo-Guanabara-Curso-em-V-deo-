class Gamer:
    def __init__(self, nick="gamer", *favgame):
        self.nick = nick
        self.favgame = list(favgame)
        
    def add_game(self, *game):
        self.favgame.extend(game)
        print(f"Jogos adicionados: {', '.join(game)}")
            
    def ficha(self):
        jogos = ', '.join(self.favgame) if self.favgame else "Nenhum jogo favorito"
        return f"Nick: {self.nick}\nJogos favoritos: {jogos}"
        
g1 = Gamer("GamerPRO", "FIFA", "CSGO")
g1.add_game("Minecraft", "GTA6")
print(g1.ficha())