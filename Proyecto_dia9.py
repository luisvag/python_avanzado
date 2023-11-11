import pygame
import random
import math
from pygame import mixer

#INICIAR PYGAME
pygame.init()

#CREAR LA PANTALLA
pantalla = pygame.display.set_mode((800, 600))

#TITULO E ICONO
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

#AGG MUSICA
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

#VARIABLES JUGADOR
img_jugador = pygame.image.load("cohete.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

#VARIABLES ENEMIGO
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

#LOOP PARA VARIOS ENEMIGOS
for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)

#VARIABLES DE LA BALA
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False

#PUNTAJE
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

#TEXTO FINAL DEL JUEGO
fuente_final = pygame.font.Font('freesansbold.ttf', 32)

def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER PAJISO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))


#FUNCION MOSTRAR PUNTAJE
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


#FUNCION JUGADOR
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


#FUNCION ENEMIGO 
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


#FUNCION DISPARO BALA
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


#FUNCION FORMULA CALCULAR CHOQUES O COLISIONES(DISTANCIA)
#D = √(x2-x1)**2 + (y2-y1)**2
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


#LOOP DEL JUEGO RECORDAR
se_ejecuta = True
while se_ejecuta:

    #RBG
    pantalla.fill((6,0,10))

    #ITERAR EVENTOS O ACCIONES
    for evento in pygame.event.get():

        #ACCION CERRAR JUEGO
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        #ACCION PRESIONAR TECLAS(FLECHAS)
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        #ACCION SOLTAR TECLAS(FLECHAS)
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #MOVER JUGADOR(MODIFICAR MOVIMIENTO)
    jugador_x += jugador_x_cambio

    #LIMITAR MOVIMIENTO JUGADOR(MANTENER DENTRO DE PANTALLA)
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    #MOVER ENEMIGO(MODIFICAR MOVIMIENTO
    for e in range(cantidad_enemigos):

        #FIN DEL JUEGO(ENDINGXD)
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

    #LIMITAR MOVIMIENTO ENEMIGO(MANTENER DENTRO DE PANTALLA)
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -1
            enemigo_y[e] += enemigo_y_cambio[e]

        #COLISION O CHOQUE
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('golpe.mp3')
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e], e)

    #MOVIMIENTO BALA
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio
    
    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x, texto_y)

    #ACTUALIZAR
    pygame.display.update()