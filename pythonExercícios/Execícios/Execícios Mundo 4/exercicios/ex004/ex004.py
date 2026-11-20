class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade
        
    def fazer_aniversario(self):
        self.idade += 1
        print(f"Parabéns, {self.nome}! Agora você tem {self.idade} anos.")

class Aluno(Pessoa):
    def __init__(self, nome="", idade=0, curso="", turma=""):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
        
    def fazer_matricula(self):
        pass
  
class Professor(Pessoa):
    def __init__(self, nome="", idade=0, especialidade="", nivel=""):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
        
    def dar_aula(self):
        pass
  
class Funcionario(Pessoa):
    def __init__(self, nome, idade=0, cargo="", setor=""):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
        
    def bater_ponto(self):
        pass
    
a1 = Aluno("José", 17, "Informatica", "T01")
print(a1.__dict__)
a1.fazer_matricula()

p1 = Professor("Carlos", 26, "TI", "Master")
p1.dar_aula
print(p1.__dict__)
p1.fazer_aniversario()
print(p1.__dict__)

f1 = Funcionario("Claudia", 34, "Atendente", "Atendimento")
f1.bater_ponto()
print(f1.__dict__)