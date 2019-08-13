import sys
import os
import time
import pygame
import random
from pygame.locals import *

pygame.init()

# Global Variables
color = pygame.Color(128, 128, 128, 128)  # background
width = 1400
height = 1400
size = (width, height)
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
estrelaImg = pygame.image.load('Estrela.png')
WHITE = (255, 255, 255)

def load_image(image_name):
    """Carrega uma imagem na memoria"""
    fullname = os.path.join(image_name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print("Cannot load image: ", fullname)
        raise SystemExit
    return image, image.get_rect()


# Play surface
playSurface = pygame.display.set_mode(size)
pygame.display.set_caption("Chinese Checkers!")
DISPLAYSURF.fill(WHITE)
DISPLAYSURF.blit(estrelaImg, (0, 0))
while True:  # main game loop

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
# Function Load Image


time.sleep(10)
