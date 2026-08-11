class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def extrato(self):
        print("Titular:", self.titular)
        print("Saldo: R$", self.saldo)

conta = ContaBancaria("Matheus", 1000)

conta.depositar(500)
conta.sacar(300)
conta.sacar(1500)

conta.extrato()