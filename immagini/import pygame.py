import pygame
import random

pygame.init()

sfondo = pygame.image.load('immagini/sfondo.png')
ucello = pygame.image.load('immagini/uccello.png')
base = pygame.image.load('immagini/base.png')
gameover = pygame.image.load('immagini/gameover.png')
tubo_giu = pygame.image.load('immagini/tubo.png')
tubo_su = pygame.transform.flip(tubo_giu, False, True)

SCHERMO = pygame.display.set_mode((288, 512))
FPS = 50
VEL_AVANZ = 2

class tubi_classe:
    def __init__(self):
       self.x = 300
       self.y = random.randint(-75,150)
    def avanza_e_disegna(self) :
        self.x -= VEL_AVANZ
        SCHERMO.blit(tubo_giu, (self.x, self.y + 210))  
        SCHERMO.blit(tubo_su, (self.x, self.y-210))
    def collisione(self, uccello, uccellox, uccelloy) :
        tolleranza = 5
        uccello_lato_dx = uccellox + uccello.get_width()-tolleranza
        uccello_lato_sx = uccellox + tolleranza
        tubi_lato_dx = self.x + tubo_giu.get_width()
        tubi_lato_sx = self.x 
        uccello_lato_su = uccelloy+ tolleranza
        uccello_lato_giu = uccelloy + uccello.get_height()-tolleranza
        tubi_lato_su = self.y+110
        tubi_lato_giu = self.y+210
        if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
            if uccello_lato_su < tubi_lato_su or uccello_lato_giu > tubi_lato_giu:
                hai_perso()


    

def disegna_oggetti():
    SCHERMO.blit(sfondo, (0,0))
    for t in tubi :
        t.avanza_e_disegna()
    SCHERMO.blit(ucello, (uccellox,uccelloy))
    SCHERMO.blit(base,(basex,400))

def aggiorna():
    pygame.display.update()  
    pygame.time.Clock().tick(FPS)
   


def inizializza():
    global uccellox, uccelloy, uccello_vely
    global basex
    global tubi
    uccellox, uccelloy = 60, 150
    uccello_vely = 0
    basex = 0
    tubi = []
    tubi.append(tubi_classe())

def hai_perso():
    SCHERMO.blit(gameover,(50,180))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:
                pygame.quit()    


inizializza()

while True:
    #Avanzamento Base
    if basex < -45: basex = 0
    basex -= VEL_AVANZ
    # Gravita                                                                                                         
    uccello_vely +=1
    if basex < -45: basex = 0
    uccelloy += uccello_vely
    #Comandi
    for event in pygame.event.get():
        if ( event.type == pygame.KEYDOWN
            and event.key == pygame.K_UP):
            uccello_vely = -10
        if event.type == pygame.QUIT:
            pygame.quit() 
    #Gestione Tubi        
    if tubi[-1].x < 150: tubi.append(tubi_classe())
    for t in tubi:
        t.collisione(ucello, uccellox, uccelloy)
    # Collisione con Base          
    if uccelloy > 380:
        hai_perso()        


    #Aggiornamento Schermo
    disegna_oggetti()
    aggiorna()
