class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depósitos
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f"A conta {self.id}, de {self.titular}, tem R${self.saldo:,.2f}."

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor:,.2f} do id {self.id} autorizado")
        
    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saldo de {self.saldo:,.2f} Insuficiente para o saque de {valor:,.2f}!")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} do id {self.id} autorizado")


c1 = ContaBancaria(112, "Guilherme", 3000)

print(c1)
c1.depositar(500)
c1.sacar(1_500_000)
print(c1)
