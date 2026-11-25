from abc import ABC, abstractmethod # Abstract Base Classes

class Funcionario(ABC):
    sal_min = 1621
    inss = 7.5
    def __init__(self, nome, sal_bruto: float | None = None , calcularEanalisar: bool = False):
        self.nome = nome
        self.sal_bruto = sal_bruto

        
    @abstractmethod
    def calc_sal(self):
        pass
    
    def analisar_sal(self):
        try:
            print(f"""Análise de Salário de {self.nome} é:
                Salário Bruto: {self.sal_bruto}
                Salário limpo de {self.salario}
                e corresponde a {self.salario / self.sal_min:.2f} salários minimos.""")
        except:
            print("Calcule um salário válido primeiro para analisá-lo")
    
    
class Horista(Funcionario):
    def __init__(self, nome, valor_hora, qtd_horas, calcularEanalisar: bool = False):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas  
        if calcularEanalisar == True:
            self.calc_sal()
            self.analisar_sal()
        
    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.qtd_horas
        self.salario = self.sal_bruto - ((self.sal_bruto * self.inss) / 100) 
        
class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto, calcularEanalisar: bool = False):
        super().__init__(nome, sal_bruto)  
        if calcularEanalisar == True:
            self.calc_sal()
            self.analisar_sal()
        
    def calc_sal(self):
        self.salario = self.sal_bruto - ((self.sal_bruto * self.inss) / 100) 




g1=Horista("Gustavo", 12, 100, False)
g1.calc_sal() 
g1.analisar_sal()

g1=Mensalista("Guilherme", 3000)
g1.calc_sal() 
g1.analisar_sal()
