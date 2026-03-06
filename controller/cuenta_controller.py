from model.cuenta import Cuenta


class CuentaController:

    def __init__(self):
        self.BD = {}
        self.contador = 1


def CrearCuenta(Titular, SaldoInicial=0):
    global contador
    if Titular == "":
        print("Error: el titular no puede estar vacío")
        return None
    try:
        SaldoInicial = float(SaldoInicial)
    except:
        print("Error: saldo inicial inválido")
        return None
    if SaldoInicial < 0:
        print("Error: el saldo inicial no puede ser negativo")
        return None
    c = {
        "id": contador,
        "titular": Titular,
        "saldo": SaldoInicial,
        "creada": str(datetime.now()),
    }
    BD[contador] = c
    contador = contador + 1
    print("Cuenta creada. ID:", c["id"], "Titular:", c["titular"], "Saldo:", c["saldo"])
    return c


def listarCuentas():
    if len(BD) == 0:
        print("No hay cuentas registradas.")
        return
    print("Listado de cuentas")
    for k in BD:
        c = BD[k]
        print(" - ID:", c["id"], "Titular:", c["titular"], "Saldo:", c["saldo"])


def Depositar(idCuenta, monto):
    if idCuenta not in BD:
        print("Error: cuenta no existe")
        return False
    try:
        monto = float(monto)
    except:
        print("Error: monto inválido")
        return False
    if monto <= 0:
        print("Error: el monto debe ser mayor que cero")
        return False
    BD[idCuenta]["saldo"] = BD[idCuenta]["saldo"] + monto
    print("Depósito realizado. Nuevo saldo:", BD[idCuenta]["saldo"])
    return True


def retirar(idCuenta, monto):
    if idCuenta not in BD:
        print("Error: cuenta no existe")
        return False
    try:
        monto = float(monto)
    except:
        print("Error: monto inválido")
        return False
    if monto <= 0:
        print("Error: el monto debe ser mayor que cero")
        return False
    if BD[idCuenta]["saldo"] < monto:
        print("Error: saldo insuficiente")
        return False
    BD[idCuenta]["saldo"] = BD[idCuenta]["saldo"] - monto
    print("Retiro realizado. Nuevo saldo:", BD[idCuenta]["saldo"])
    return True


def buscarCuentaPorTitular(nombre):
    res = []
    for k in BD:
        if BD[k]["titular"].lower() == nombre.lower():
            res.append(BD[k])
    return res
