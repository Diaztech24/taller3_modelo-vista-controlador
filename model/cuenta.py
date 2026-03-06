from datetime import datetime


class Cuenta:


    def __init__(self, cuenta_id: int, titular: str, saldo: float = 0):

        self.id = cuenta_id
        self.titular = titular
        self.saldo = saldo
        self.creada = datetime.now()

    def depositar(self, monto: float):

        self.saldo += monto

    def retirar(self, monto: float):

        self.saldo -= monto