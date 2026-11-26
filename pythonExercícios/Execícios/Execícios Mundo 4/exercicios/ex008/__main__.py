from ex008 import ContaBancaria

def main():
    c1 = ContaBancaria(112, "Guilherme", 3000)

    #print(c1)
    c1.depositar(500)
    c1.sacar(100)
    c1.titular = "Jonas"
    c1._titular = "Jonas" # Ele deixa, mas não mexa pois 'Adultos estãg consentindo'...
    c1.saldo = 0
    c1.__saldo = 0 # Não mexe
    c1._ContaBancaria__saldo = 0 # Ele deixa, mas não mexa pois 'Adultos estãg consentindo'...
    print(c1)

if __name__ == "__main__":
    main()
    