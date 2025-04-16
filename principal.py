from numeros import generador_c, generador_m, generador_p, agregar_texto


@agregar_texto
def dar_turno(g):
    print(next(g))


def principal():

    gp = generador_p()
    gm = generador_m()
    gc = generador_c()

    print("BIENVENIDO AL SISTEMA DE TURNOS\n")

    while True:

        print("1) Sacar turno")
        print("2) Salir\n")
        opcion = input("Seleccione su opcion: ")

        if opcion == "1":

            while True:

                print("\n1) Perfume")
                print("2) Medicamentos")
                print("3) Cosmeticos\n")
                opcion_2 = input("Seleccione un area de compras\n")

                if opcion_2 == "1":
                    dar_turno(gp)

                elif opcion_2 == "2":
                    dar_turno(gm)

                elif opcion_2 == "3":
                    dar_turno(gc)
                else:
                    print("Ingrese una opcion valida")

                opcion_3 = input("Otro turno? (si/no)")

                if opcion_3 == "si":
                    continue
                else:
                    break

        else:
            print("Vuelva pronto")
            break


principal()
