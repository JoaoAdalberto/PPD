import pygame
import sys
import os
from pygame.locals import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Drawing')

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
DISPLAYSURF.fill(WHITE)
pygame.draw.circle(DISPLAYSURF, GREEN, (328, 46), 10)
pygame.draw.circle(DISPLAYSURF, GREEN, (317, 65), 10)
pygame.draw.circle(DISPLAYSURF, GREEN, (339, 65), 10)
pygame.draw.circle(DISPLAYSURF, GREEN, (306, 84), 10)
pygame.draw.circle(DISPLAYSURF, GREEN, (328, 84), 10)
pygame.draw.circle(DISPLAYSURF, GREEN, (350, 84), 10)
pygame.draw.circle(DISPLAYSURF, GREEN, (295, 103), 10)
pygame.draw.circle(DISPLAYSURF, GREEN, (317, 103), 10)
pygame.draw.circle(DISPLAYSURF, GREEN, (339, 103), 10)
pygame.draw.circle(DISPLAYSURF, GREEN, (361, 103), 10)

class criaCirculo:
    def __init__(self, x, y, cor, raio, moveu=False):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.moveu = moveu

    def cria_circulo(self, surface):
        return pygame.draw.circle(surface, self.cor, (self.x, self.y), self.raio)


def load_image(image_name):
    """Carrega uma imagem na memoria"""
    fullname = os.path.join(image_name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print("Cannot load image: ", fullname)
        raise SystemExit
    return image, image.get_rect()


load_image("Estrela.png")
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()