from abc import ABC, abstractmethod # Abstract Base Classes

class Pessoa(ABC):
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade
        
    def fazer_aniversario(self):
        self.idade += 1
        print(f"Parabéns, {self.nome}! Agora você tem {self.idade} anos.")

    @abstractmethod
    def estudar(self):
        pass

    
class Aluno(Pessoa):
    def __init__(self, nome="", idade=0, curso="", turma=""):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
        
    def fazer_matricula(self):
        print(f"{self.nome} está matriculado no curso de {self.curso}, turma {self.turma}.")
    
    def estudar(self):
        print(f"{self.nome} está estudando {self.curso}.")

class Professor(Pessoa):
    def __init__(self, nome="", idade=0, especialidade="", nivel=""):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
        
    def dar_aula(self):
        print(f"{self.nome} está dando aula de {self.especialidade}.")

    def estudar(self):
        print(f"{self.nome} está estudando {self.especialidade}.")
  
class Funcionario(Pessoa):
    def __init__(self, nome, idade=0, cargo="", setor=""):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
        
    def bater_ponto(self):
        print(f"{self.nome} bateu o ponto no setor {self.setor}.")
    
    def estudar(self):
        print(f"{self.nome} está estudando para melhorar no cargo de {self.cargo}.")