from zipfile import ZipFile
import os
import re
from datetime import date
import time
import math


# Recorrer archivos
# abrir archivo
# leer archivo
# revisar coincidencia
# Tiempo de busqueda

lista_coin = []


def buscar_coincidencias(ruta):
    nombre_archivo = ruta[46:]
    if len(nombre_archivo) == 12:
        nombre_archivo = nombre_archivo+" "
    patron = r'N[a-zA-Z]{3}-\d{5}'
    archivo = open(ruta, "r")
    texto = archivo.read()
    concidencia = re.search(patron, texto)
    if concidencia != None:
        linea = f"{nombre_archivo}   {concidencia.group()}"
        return linea
    else:
        False


def busqueda_nserie():

    principal = "Mi_Gran_Directorio"
    for carpeta, subcarpeta, archivos in os.walk(principal):
        for nombre_arch in archivos:
            ruta = (f"{carpeta}\\{nombre_arch}")
            coincidencia = buscar_coincidencias(ruta)
            if coincidencia:
                lista_coin.append(coincidencia)


def imprimir_tabla():
    inicio = time.time()
    busqueda_nserie()

    print("----------------------------")
    hoy = date.today()
    print(f"La fecha de hoy es: {hoy.day}/{hoy.month}/{hoy.year}\n")

    print(" ARCHIVO        NRO. SERIE")
    print(" -------        ----------")
    for linea in lista_coin:
        print(linea)
    print(f"\nNumeros Encontrados: {len(lista_coin)}")

    final = time.time()
    print(f"Tiempo de ejecuccion: {math.ceil(final-inicio)} segundo")
    print("----------------------------")


imprimir_tabla()
