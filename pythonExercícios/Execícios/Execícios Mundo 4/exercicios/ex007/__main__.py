import inspect

from classes import  Pessoa, Aluno, Professor, Funcionario
   
def main():
    a1 = Aluno("José", 17, "Informatica", "T01")
    a1.fazer_aniversario()
    a1.fazer_matricula()

    p1 = Professor("Carlos", 26, "TI", "Master")
    p1.dar_aula()
    p1.fazer_aniversario()


    f1 = Funcionario("Claudia", 34, "Atendente", "Atendimento")
    f1.bater_ponto()
    f1.fazer_aniversario()
    f1.estudar()
    
    
if __name__ == "__main__":
    main()