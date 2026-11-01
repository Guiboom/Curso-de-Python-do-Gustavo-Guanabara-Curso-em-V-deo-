class Funcionario:
    def __init__(self, nome="", setor="", cargo=""):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        
    def apresentar(self):
        return(f"Olá, Meu nome é {self.nome}, sou do setor de {self.setor} e meu cargo é {self.cargo}.")
    
p1funcionario = Funcionario("Fabiam", "Cargas", "Descarga")

print(funcionario.apresentar())