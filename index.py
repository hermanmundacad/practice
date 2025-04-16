from pathlib import Path
from os import system


def bienvenida(ruta):

    cantidad = 0

    for archivos in Path(ruta).glob("**/*.txt"):
        cantidad += 1

    print("\nBienvenidos al Recetario Virtual \n")
    print(f"Las recetas estan en: {ruta}\n")
    print(f"Tienes {cantidad} recetas archivadas.\n")


def desplegar_menu():

    print("[1] - leer receta")
    print("[2] - crear receta")
    print("[3] - crear categoria")
    print("[4] - eliminar receta")
    print("[5] - eliminar categoria")
    print("[6] - finalizar programa\n")
    opcion = input("Seleccione una de las opciones:")
    system("cls")
    return opcion


def mostrar_categorias(ruta):

    contador = 1
    categorias = []
    print("Estas son las categorias: \n")
    for carpeta in Path(ruta).iterdir():
        str_carpeta = str(carpeta.name)
        print(f"{contador}) {str_carpeta}\n")
        categorias.append(str_carpeta)
        contador += 1
    opcion = int(input("Indique la categoria: "))
    system("cls")
    return categorias[opcion-1]


def mostrar_recetas(ruta, categoria):
    contador = 1
    recetas = []

    ruta = Path(ruta, categoria)

    print("Estas son las recetas de esta categoria: \n")
    for receta in ruta.glob("*.txt"):
        str_receta = str(receta.name)
        print(f"{contador}) {str_receta}\n")
        recetas.append(str_receta)
        contador += 1
    opcion = int(input("Indique la receta: "))
    system("cls")
    return recetas[opcion-1]


def leer_receta(ruta):
    categoria = mostrar_categorias(ruta)

    receta = mostrar_recetas(ruta, categoria)

    ruta = Path(ruta, categoria, receta)

    print("El contenido de su receta es: \n")
    print(ruta.read_text(), "\n")


def crear_receta(ruta):

    categoria = mostrar_categorias(ruta)
    nombre = input("Indique el nombre de su receta: \n")
    receta = input("Ingrese el contenido de su receta: \n")
    nombre = str(nombre+".txt")
    ruta = Path(ruta, categoria, nombre)
    ruta.write_text(receta)


def crear_categoria(ruta):
    nombre = input("Indique el nombre de su categoria: \n")

    ruta = Path(ruta, nombre)
    ruta.mkdir()


def eliminar_receta(ruta):
    categoria = mostrar_categorias(ruta)
    receta = mostrar_recetas(ruta, categoria)
    ruta = Path(ruta, categoria, receta)
    ruta.unlink()


def eliminar_categoria(ruta):
    categoria = mostrar_categorias(ruta)
    ruta2 = Path(ruta, categoria)
    for receta in ruta2.glob("*.txt"):
        print("hola")
        receta.unlink()
    ruta = Path(ruta, categoria)
    ruta.rmdir()


######################################################
ruta = Path("C:/Users/herma/OneDrive/Escritorio/CURSO PY/Recetas")


bienvenida(ruta)
while True:

    opcion = desplegar_menu()

    if opcion == "1":
        leer_receta(ruta)
    elif opcion == "2":
        crear_receta(ruta)
    elif opcion == "3":
        crear_categoria(ruta)
    elif opcion == "4":
        eliminar_receta(ruta)
    elif opcion == "5":
        eliminar_categoria(ruta)
    elif opcion == "6":
        break
    else:
        print("Vuelva a intentar, ingresando una opcion valida\n")

    opcion = input("Desea seguir ocupando el programa? (si/no) ")
    system("cls")
    if opcion.lower() == "si":
        continue
    else:
        break
