import pygame
import random

#INICIAR PYGAME
pygame.init()

#CREA LA PANTALLA
pantalla = pygame.display.set_mode((800,600))

#TITULO E ICONO
pygame.display.set_caption('Invasion Espacial')
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)

#VARIABLES JUGADOR
img_jugador = pygame.image.load('cohete.png')
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0

#VARIABLES ENEMIGOS
img_enemigo = pygame.image.load('enemigo.png')
enemigo_x = random.randint(0,736)
enemigo_y = random.randint(50,200)
enemigo_x_cambio = 0.5
enemigo_y_cambio = 50

#VARIABLES DE LA BALA 
img_bala = pygame.image.load('bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

#FUNCION JUGADOR
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

#FUNCION ENEMIGO
def enemigo(x,y):
    pantalla.blit(img_enemigo,(x,y))

#FUNCION DISPARO BALA
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x+16,y+10))

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
                jugador_x_cambio = -0.5
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.5
            if evento.key == pygame.K_SPACE:
                if bala_visible == False:
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
    
    #MOVER ENEMIGO(MODIFICAR MOVIMIENTO)     
    enemigo_x += enemigo_x_cambio  

    #LIMITAR MOVIMIENTO ENEMIGO(MANTENER DENTRO DE PANTALLA)
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.5
    elif enemigo_x >= 736:
        enemigo_x_cambio = -0.5

    #MOVIMIENTO BALA
    if bala_y <= 0:
        bala_y = 500
        bala_visible = False

    if bala_visible == True:
        disparar_bala(bala_x,bala_y)
        bala_y -= bala_y_cambio

    jugador(jugador_x,jugador_y)
    enemigo(enemigo_x,enemigo_y)
    

    #ACTUALIZAR
    pygame.display.update() 
