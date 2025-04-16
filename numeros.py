def generador_p():
    n = 1
    while True:
        if n < 10:
            yield f"P-0{n}"
            n += 1
        else:
            yield f"P-{n}"
            n += 1


def generador_m():
    n = 1
    while True:
        if n < 10:
            yield f"M-0{n}"
            n += 1
        else:
            yield f"M-{n}"
            n += 1


def generador_c():
    n = 1
    while True:
        if n < 10:
            yield f"C-0{n}"
            n += 1
        else:
            yield f"C-{n}"
            n += 1


def agregar_texto(funcion):

    def funcion_con_texto(g):

        print("Su turno es: \n")
        funcion(g)
        print("\n Aguarde y sera atendido\n")

    return funcion_con_texto
