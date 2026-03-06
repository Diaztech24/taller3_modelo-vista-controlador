from datetime import datetime
from model.cuenta import Cuenta


class CuentaController:


    def __init__(self):
        self.BD = {}
        self.contador = 1

    def CrearCuenta(self, Titular, SaldoInicial=0):
        if Titular == "":
            print("Error: el titular no puede estar vacío")
            return None

        try:
            SaldoInicial = float(SaldoInicial)
        except ValueError:
            print("Error: saldo inicial inválido")
            return None

        if SaldoInicial < 0:
            print("Error: el saldo inicial no puede ser negativo")
            return None

        c = {
            "id": self.contador,
            "titular": Titular,
            "saldo": SaldoInicial,
            "creada": str(datetime.now()),
        }

        self.BD[self.contador] = c
        self.contador += 1

        print("Cuenta creada. ID:", c["id"], "Titular:", c["titular"], "Saldo:", c["saldo"])
        return c

    def listarCuentas(self):
        if len(self.BD) == 0:
            print("No hay cuentas registradas.")
            return

        print("Listado de cuentas")
        for k in self.BD:
            c = self.BD[k]
            print(" - ID:", c["id"], "Titular:", c["titular"], "Saldo:", c["saldo"])

    def Depositar(self, idCuenta, monto):
        if idCuenta not in self.BD:
            print("Error: cuenta no existe")
            return False

        try:
            monto = float(monto)
        except ValueError:
            print("Error: monto inválido")
            return False

        if monto <= 0:
            print("Error: el monto debe ser mayor que cero")
            return False

        self.BD[idCuenta]["saldo"] += monto
        print("Depósito realizado. Nuevo saldo:", self.BD[idCuenta]["saldo"])
        return True

    def retirar(self, idCuenta, monto):
        if idCuenta not in self.BD:
            print("Error: cuenta no existe")
            return False

        try:
            monto = float(monto)
        except ValueError:
            print("Error: monto inválido")
            return False

        if monto <= 0:
            print("Error: el monto debe ser mayor que cero")
            return False

        if self.BD[idCuenta]["saldo"] < monto:
            print("Error: saldo insuficiente")
            return False

        self.BD[idCuenta]["saldo"] -= monto
        print("Retiro realizado. Nuevo saldo:", self.BD[idCuenta]["saldo"])
        return True

    def buscarCuentaPorTitular(self, nombre):
        res = []

        for k in self.BD:
            if self.BD[k]["titular"].lower() == nombre.lower():
                res.append(self.BD[k])

        return res