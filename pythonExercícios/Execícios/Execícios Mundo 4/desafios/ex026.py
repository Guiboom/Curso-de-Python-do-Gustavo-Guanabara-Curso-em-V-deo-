from abc import ABC, abstractmethod # Abstract Base Classes

class Funcionario(ABC):
    sal_min = 1621
    inss = 7.5
    def __init__(self, nome, sal_bruto):
        self.nome = nome
        self.sal_bruto = sal_bruto

        
    @abstractmethod
    def calc_sal(self):
        pass
    
    def analisar_sal(self):
        print(f"Análise de Salário: salário de {self.nome} é de {self.salario} e corresponde a {self.salario / sal_min} salários minimos.")
    
class Horista(Funcionario):
    def __init__(self, nome, valor_hora, qtd_horas ):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas

        
    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.qtd_horas
        self.salario = self.sal_bruto - ((self.sal_bruto * self.inss) / 100) 
        self.analisar_sal()


g1=Horista("Gustavo", 12, 100)




