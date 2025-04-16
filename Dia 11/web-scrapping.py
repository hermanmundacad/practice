import bs4
import requests

# url sin numero de pagina
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos 4 o 5 estrellas

lista_ratings_altos = []

# iterar paginas

for pagina in range(1, 3):

    # crear sopa en cada pagina

    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    # seleccionar datos de los libros

    libros = sopa.select(".product_pod")

    # iterar libros

    for libro in libros:

        # chequear que tengan 4 o 5 estrellas

        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:

            # guardar titulo en variable

            titulo_libro = libro.select("a")[1]["title"]
            lista_ratings_altos.append(titulo_libro)

# ver libros de 4 y 5 estrella en consola

for t in lista_ratings_altos:
    print(t)
