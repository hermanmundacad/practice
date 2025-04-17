from math import pi


def area_rectangulo(alto, largo):
    area = alto*largo
    print(f"El area del rectangulo es {area}")
    return None


def area_circulo(r):
    area = pi*r**2
    print(f"El area del circulo es {area}")
    return None


def area_triangulo(h, base):
    area = h*base/2
    print(f"El area del triangulo es {area}")
    return None


while True:

    print("\n1) Rectangulo")
    print("2) Circulo")
    print("3) Triangulo")
    print("4) Salir \n")
    figura = input("El area de que figura desea calcular? \n")

    if figura.lower() == "1":
        alto = int(input("Indique el alto del rectangulo \n"))
        largo = int(input("Indique el largo del rectangulo \n"))
        area_rectangulo(alto, largo)

    elif figura.lower() == "2":
        radio = int(input("Indique el radio del circulo \n"))
        area_circulo(radio)
    elif figura.lower() == "3":
        altura = int(input("Indique la altura del triangulo \n"))
        base = int(input("Indique la base del rectangulo \n"))
        area_rectangulo(altura, base)
    else:
        break
