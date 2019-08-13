import sys
import os
import pygame
import random
from pygame.locals import *

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
highlightcolor = blue


class tabuleiro:
    def __init__(self, surface, x, y, cor, raio=15, moveu=False):
        self.surface = surface
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.moveu = moveu

    def cria_circulo(self):
        return pygame.draw.circle(self.surface, self.cor, (self.x, self.y), self.raio)

tabuleiro.cria_circulo()


    @property
    def cor(self):
        return self.cor
