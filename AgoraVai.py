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
FPS = 30
circulos = []
MOUSE_LEFT = 1
MOUSE_RIGHT = 3
windowwidth = 1200
windowheight = 800
size = (windowwidth, windowheight)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (128, 128, 128)
lista = [[], []]
listadecor = []
highlightcolor = blue
color = pygame.Color
pygame.init()
playSurface = pygame.display.set_mode(size)
playSurface.fill(grey)
tabuleiro = Tabuleiro()
tabuleiro.desenha_estrela(playSurface)


bolas_selecionadas = []

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == MOUSE_LEFT:
                    position_mouse = pygame.mouse.get_pos()
                    x = position_mouse[0]
                    y = position_mouse[1]
                    circulo = tabuleiro.verifica_posicao_na_matriz(x, y)
                    if circulo is not None:
                        if circulo.get_cor() != white and len(circulos) == 0:
                            circulos.append(circulo)
                        if circulo.get_cor() == white and len(circulos) > 0:
                            circulos.append(circulo)
                    if len(circulos) == 2:
                        tabuleiro.muda_posicao_circulo(circulos[0], circulos[1])
                        circulos = []
                    tabuleiro.desenha_estrela(playSurface)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == MOUSE_RIGHT:
                position_mouse = pygame.mouse.get_pos()
                x = position_mouse[0]
                y = position_mouse[1]
                circulo = tabuleiro.verifica_posicao_na_matriz(x, y)
                if circulo is not None and circulo.get_cor() != white:
                    vizinhanca = tabuleiro.pega_vizinhos(circulo)
                    tabuleiro.desenha_estrela(playSurface)

        if event.type == pygame.KEYDOWN:
            pygame.display.flip()




