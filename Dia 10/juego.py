import pygame
import random
import math
from pygame import mixer

pygame.init()

# Crear Pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.jpg")

# Variables del jugador
imagen_jugador = pygame.image.load("nave-espacial.png")
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0

# Variables del enemigo
imagen_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

# Variables del enemigo

for e in range(cantidad_enemigos):
    imagen_enemigo.append(pygame.image.load("ufo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.17)
    enemigo_y_cambio.append(50)

# variable bala
imagen_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 0
bala_y_cambio = -2
hay_bala = False


puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10


def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

# funcion jugador


def jugador(x, y):
    pantalla.blit(imagen_jugador, (x, y))

# funcion enemigo


def enemigo(x, y, ene):
    pantalla.blit(imagen_enemigo[ene], (x, y))


def disparar_bala(x, y):
    global hay_bala
    hay_bala = True
    pantalla.blit(imagen_bala, (x, y))


def hay_colision(x1, x2, y1, y2):

    distancia = math.sqrt(math.pow((x1-x2), 2) + math.pow((y2-y1), 2))
    if distancia < 27:
        return True
    else:
        return False


def texto_final():
    fuente = pygame.font.Font("freesansbold.ttf", 70)
    texto = fuente.render(f"Game Over", True, (255, 255, 255))
    pantalla.blit(texto, (250, 300))


se_ejecuta = True

while se_ejecuta:

    # colorear
    pantalla.blit(fondo, (0, 0))

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.2

            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.2

            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")
                if hay_bala == False:
                    sonido_bala.play()
                    bala_x = jugador_x + 16
                    bala_y = jugador_y
                    disparar_bala(bala_x, bala_y)

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # movimiento
    jugador_x += jugador_x_cambio

    # paredes
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # ubicacion
    for e in range(cantidad_enemigos):

        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break
        enemigo_x[e] += enemigo_x_cambio[e]
    # movimiento enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.17
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.17
            enemigo_y[e] += enemigo_y_cambio[e]
        colision = hay_colision(enemigo_x[e], bala_x, enemigo_y[e], bala_y)
        if colision:
            sonido_golpe = mixer.Sound("golpe.mp3")
            sonido_golpe.play()
            bala_y = 500
            hay_bala = False
            puntaje += 1

            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # movimiento bala
    if bala_y <= -64:
        bala_y = 500
        hay_bala = False

    if hay_bala == True:
        bala_y += bala_y_cambio
        disparar_bala(bala_x, bala_y)

    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x, texto_y)

    pygame.display.update()
