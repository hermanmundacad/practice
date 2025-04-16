from random import randint
from os import system


class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self.balance = 0
        self.numero_cuenta = generar_numero_cuenta()

    def __str__(self):
        mensaje = (
            f"Cliente: {self.nombre} {self.apellido}\n"
            f"N° de cuenta: {self.numero_cuenta}\n"
            f"Balance: {self.balance}"
        )
        return mensaje

    def depositar(self, monto):
        self.balance += monto
        print(f"Se han depositado ${monto} a su cuenta")

    def retirar(self, monto):
        self.balance -= monto
        print(f"Se han retirado ${monto} a su cuenta")


def generar_numero_cuenta():
    n_cuenta = ""
    for i in range(8):
        n_cuenta += str(randint(0, 9))
    return int(n_cuenta)


def crear_cliente(nombre, apellido):

    return Cliente(nombre, apellido)


def inicio():

    print("Bienvenido al programa tu banco\n")

    nombre = input("Ingrese su nombre: \n")
    apellido = input("Ingrese su apellido: \n")

    cliente = crear_cliente(nombre, apellido)

    system("cls")
    while True:

        print("1) Ver estado de cuenta")
        print("2) Depositar")
        print("3) Retirar")
        print("4) Salir del Programa\n")

        opcion = input("Desea hacer alguna operacion:")
        system("cls")

        if opcion == "1":
            print(cliente, "\n")

        elif opcion == "2":
            monto = int(input("Cuanto dinero desea depositar: "))
            cliente.depositar(monto)

        elif opcion == "3":
            while True:
                monto = int(input("Cuanto dinero desea retirar: "))
                if cliente.balance < monto:
                    print(" No es posible retirar mas que el dinero que tiene")
                else:
                    cliente.retirar(monto)
                    break
        elif opcion == "4":
            break


inicio()
