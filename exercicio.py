class ContaBancaria:
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo
        self.transacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append(f"Depósito de {valor:.2f}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.transacoes.append(f"Saque de {valor:.2f}")
        else:
            print("Saldo insuficiente.")

    def extrato(self):
        print(f"Extrato da conta de {self.nome}:")
        for transacao in self.transacoes:
            print(transacao)
        print(f"Saldo atual: {self.saldo:.2f}")


# Exemplo de uso
conta = ContaBancaria("João")
conta.depositar(1000)
conta.sacar(500)
conta.sacar(700)  # Isso deve imprimir "Saldo insuficiente."
conta.extrato()
