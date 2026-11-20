from classeex005 import  Aluno, Professor, Funcionario
   
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