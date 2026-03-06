# ============================================================
# ACTIVIDAD – SCRIPT INICIAL (VERSIÓN SIN BUENAS PRÁCTICAS)
# ============================================================
# Qué hace este script:
#
# Este programa implementa un sistema muy simple de cuentas bancarias
# en consola. Permite:
#   1) Crear cuentas (titular + saldo inicial)
#   2) Consultar el listado de cuentas
#   3) Depositar dinero
#   4) Retirar dinero
#
# Importante:
# - Todo está en un solo archivo.
# - Mezcla lógica, datos y salida por consola.
# - No sigue estándares de estilo.
# - No tiene docstrings.
# - Usa nombres inconsistentes y estructura poco clara.
#

# - Formatee el código y corrija problemas de estilo con Ruff
# - Agregue docstrings (modelo, controlador, vista)
# - Reestructure el proyecto a MVC:
#     model/cuenta.py
#     view/consola.py
#     controller/cuenta_controller.py
#     main.py
#
# Nota: este archivo debe seguir funcionando antes y después del refactor.
# ============================================================
from controller.cuenta_controller import CuentaController
from view.consola import mostrar_menu


def main():
    while True:
        menu()
        op = input("Seleccione una opción: ").strip()
        if op == "1":
            t = input("Titular: ").strip()
            s = input("Saldo inicial: ").strip()
            CrearCuenta(t, s)
        elif op == "2":
            listarCuentas()
        elif op == "3":
            try:
                i = int(input("ID cuenta: ").strip())
            except:
                print("Error: ID inválido")
                continue
            m = input("Monto a depositar: ").strip()
            Depositar(i, m)
        elif op == "4":
            try:
                i = int(input("ID cuenta: ").strip())
            except:
                print("Error: ID inválido")
                continue
            m = input("Monto a retirar: ").strip()
            retirar(i, m)
        elif op == "5":
            n = input("Titular: ").strip()
            encontrados = buscarCuentaPorTitular(n)
            if len(encontrados) == 0:
                print("No se encontraron cuentas para ese titular.")
            else:
                print("Cuentas encontradas:")
                for c in encontrados:
                    print(
                        " - ID:", c["id"], "Saldo:", c["saldo"], "Creada:", c["creada"]
                    )
        elif op == "0":
            print("Finalizando programa.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
