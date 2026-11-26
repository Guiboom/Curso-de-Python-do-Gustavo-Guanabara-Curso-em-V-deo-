class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depósitos
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id # publico (+)
        self._titular = nome # Protegido (#)
        self.__saldo = saldo # Privado (-)
        print(f"Conta {self.id}, de {self._titular}, com saldo de {self.__saldo:,.2f} criada com sucesso!")
    
    def __str__(self):
        #return f"A conta {self.id}, de {self.titular}, tem R${self.saldo:,.2f}."
        return f"Estado atual da conta {self.__dict__}"

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Deposito de R${valor:,.2f} do id {self.id} autorizado")
        
    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f"Saldo de {self.__saldo:,.2f} Insuficiente para o saque de {valor:,.2f}!")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:,.2f} do id {self.id} autorizado")



