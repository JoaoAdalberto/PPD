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


class Bola():
    def __init__(self, cor, x, y, raio=10, moveu=False):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.moveu = moveu

    def get_cor(self):
        return self.cor

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def cria_bola(self, surface):
        return pygame.draw.circle(surface, self.cor, (self.x, self.y), self.raio)
