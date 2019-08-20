import sys
import os
import pygame
import math
import random
import numpy as np
from tabuleiro import Tabuleiro
from bolas import Bola
from pygame.locals import *
from tkinter import *
from tkinter import ttk
from pygame import Surface

# Global Variables
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (128, 128, 128)


class Botao():
    def __init__(self, texto, cor, cor_do_texto):
        pygame.init()
        self.texto = texto
        self.cor = cor
        self.cor_do_texto = cor_do_texto
        self.font = pygame.font.SysFont("Arial", 20, bold=True)

    def desenha_botao(self, playSurface, x, y, largura, altura):
        rect = pygame.draw.rect(playSurface, self.cor, (x, y, largura, altura))
        render_font = self.font.render(self.texto, True, self.cor_do_texto)
        largura_do_texto, altura_do_texto = render_font.get_size()
        posicao_fonte_x = (x + largura/2) - (largura_do_texto/2)
        posicao_fonte_y = (y - altura/2) - (altura_do_texto / 2)
        playSurface.blit(render_font, (posicao_fonte_x, posicao_fonte_y))
        pygame.display.flip()
        return rect
