import sys
import os
import pygame
import math
import random
import numpy as np
from pygame.locals import *
from tkinter import *
from tkinter import ttk

# Global Variables


FPS = 30
windowwidth = 1200
windowheight = 800
size = (windowwidth, windowheight)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (128, 128, 128)
lista = [[],[]]
listadecor = []
highlightcolor = blue
color = pygame.Color(255, 255, 255)
pygame.init()
playSurface = pygame.display.set_mode(size)
playSurface.fill(grey)
mousex = 0
mousey = 0

bolas = np.array(
    [pygame.draw.circle(playSurface, green, (328, 46), 10), pygame.draw.circle(playSurface, green, (317, 65), 10),
     pygame.draw.circle(playSurface, green, (339, 65), 10),
     pygame.draw.circle(playSurface, green, (306, 84), 10), pygame.draw.circle(playSurface, green, (328, 84), 10),
     pygame.draw.circle(playSurface, green, (350, 84), 10),
     pygame.draw.circle(playSurface, green, (295, 103), 10), pygame.draw.circle(playSurface, green, (317, 103), 10),
     pygame.draw.circle(playSurface, green, (339, 103), 10), pygame.draw.circle(playSurface, green, (361, 103), 10),
     pygame.draw.circle(playSurface, white, (196, 122), 10),
     pygame.draw.circle(playSurface, white, (218, 122), 10),
     pygame.draw.circle(playSurface, white, (240, 122), 10),
     pygame.draw.circle(playSurface, white, (262, 122), 10),
     pygame.draw.circle(playSurface, white, (284, 122), 10),
     pygame.draw.circle(playSurface, white, (306, 122), 10),
     pygame.draw.circle(playSurface, white, (328, 122), 10),
     pygame.draw.circle(playSurface, white, (350, 122), 10),
     pygame.draw.circle(playSurface, white, (372, 122), 10),
     pygame.draw.circle(playSurface, white, (394, 122), 10),
     pygame.draw.circle(playSurface, white, (416, 122), 10),
     pygame.draw.circle(playSurface, white, (438, 122), 10),
     pygame.draw.circle(playSurface, white, (460, 122), 10),
     pygame.draw.circle(playSurface, white, (207, 141), 10),
     pygame.draw.circle(playSurface, white, (229, 141), 10),
     pygame.draw.circle(playSurface, white, (251, 141), 10),
     pygame.draw.circle(playSurface, white, (273, 141), 10),
     pygame.draw.circle(playSurface, white, (295, 141), 10),
     pygame.draw.circle(playSurface, white, (317, 141), 10),
     pygame.draw.circle(playSurface, white, (339, 141), 10),
     pygame.draw.circle(playSurface, white, (361, 141), 10),
     pygame.draw.circle(playSurface, white, (383, 141), 10),
     pygame.draw.circle(playSurface, white, (405, 141), 10),
     pygame.draw.circle(playSurface, white, (427, 141), 10),
     pygame.draw.circle(playSurface, white, (449, 141), 10),
     pygame.draw.circle(playSurface, white, (218, 160), 10),
     pygame.draw.circle(playSurface, white, (240, 160), 10),
     pygame.draw.circle(playSurface, white, (262, 160), 10),
     pygame.draw.circle(playSurface, white, (284, 160), 10),
     pygame.draw.circle(playSurface, white, (306, 160), 10),
     pygame.draw.circle(playSurface, white, (328, 160), 10),
     pygame.draw.circle(playSurface, white, (350, 160), 10),
     pygame.draw.circle(playSurface, white, (372, 160), 10),
     pygame.draw.circle(playSurface, white, (394, 160), 10),
     pygame.draw.circle(playSurface, white, (416, 160), 10),
     pygame.draw.circle(playSurface, white, (438, 160), 10),
     pygame.draw.circle(playSurface, white, (229, 179), 10),
     pygame.draw.circle(playSurface, white, (251, 179), 10),
     pygame.draw.circle(playSurface, white, (273, 179), 10),
     pygame.draw.circle(playSurface, white, (295, 179), 10),
     pygame.draw.circle(playSurface, white, (317, 179), 10),
     pygame.draw.circle(playSurface, white, (339, 179), 10),
     pygame.draw.circle(playSurface, white, (361, 179), 10),
     pygame.draw.circle(playSurface, white, (383, 179), 10),
     pygame.draw.circle(playSurface, white, (405, 179), 10),
     pygame.draw.circle(playSurface, white, (427, 179), 10),
     pygame.draw.circle(playSurface, white, (240, 198), 10),
     pygame.draw.circle(playSurface, white, (262, 198), 10),
     pygame.draw.circle(playSurface, white, (284, 198), 10),
     pygame.draw.circle(playSurface, white, (306, 198), 10),
     pygame.draw.circle(playSurface, white, (328, 198), 10),
     pygame.draw.circle(playSurface, white, (350, 198), 10),
     pygame.draw.circle(playSurface, white, (372, 198), 10),
     pygame.draw.circle(playSurface, white, (394, 198), 10),
     pygame.draw.circle(playSurface, white, (416, 198), 10),
     pygame.draw.circle(playSurface, white, (229, 217), 10),
     pygame.draw.circle(playSurface, white, (251, 217), 10),
     pygame.draw.circle(playSurface, white, (273, 217), 10),
     pygame.draw.circle(playSurface, white, (295, 217), 10),
     pygame.draw.circle(playSurface, white, (317, 217), 10),
     pygame.draw.circle(playSurface, white, (339, 217), 10),
     pygame.draw.circle(playSurface, white, (361, 217), 10),
     pygame.draw.circle(playSurface, white, (383, 217), 10),
     pygame.draw.circle(playSurface, white, (405, 217), 10),
     pygame.draw.circle(playSurface, white, (427, 217), 10),
     pygame.draw.circle(playSurface, white, (218, 236), 10),
     pygame.draw.circle(playSurface, white, (240, 236), 10),
     pygame.draw.circle(playSurface, white, (262, 236), 10),
     pygame.draw.circle(playSurface, white, (284, 236), 10),
     pygame.draw.circle(playSurface, white, (306, 236), 10),
     pygame.draw.circle(playSurface, white, (328, 236), 10),
     pygame.draw.circle(playSurface, white, (350, 236), 10),
     pygame.draw.circle(playSurface, white, (372, 236), 10),
     pygame.draw.circle(playSurface, white, (394, 236), 10),
     pygame.draw.circle(playSurface, white, (416, 236), 10),
     pygame.draw.circle(playSurface, white, (438, 236), 10),
     pygame.draw.circle(playSurface, white, (207, 255), 10),
     pygame.draw.circle(playSurface, white, (229, 255), 10),
     pygame.draw.circle(playSurface, white, (251, 255), 10),
     pygame.draw.circle(playSurface, white, (273, 255), 10),
     pygame.draw.circle(playSurface, white, (295, 255), 10),
     pygame.draw.circle(playSurface, white, (317, 255), 10),
     pygame.draw.circle(playSurface, white, (339, 255), 10),
     pygame.draw.circle(playSurface, white, (361, 255), 10),
     pygame.draw.circle(playSurface, white, (383, 255), 10),
     pygame.draw.circle(playSurface, white, (405, 255), 10),
     pygame.draw.circle(playSurface, white, (427, 255), 10),
     pygame.draw.circle(playSurface, white, (449, 255), 10),
     pygame.draw.circle(playSurface, white, (196, 274), 10),
     pygame.draw.circle(playSurface, white, (218, 274), 10),
     pygame.draw.circle(playSurface, white, (240, 274), 10),
     pygame.draw.circle(playSurface, white, (262, 274), 10),
     pygame.draw.circle(playSurface, white, (284, 274), 10),
     pygame.draw.circle(playSurface, white, (306, 274), 10),
     pygame.draw.circle(playSurface, white, (328, 274), 10),
     pygame.draw.circle(playSurface, white, (350, 274), 10),
     pygame.draw.circle(playSurface, white, (372, 274), 10),
     pygame.draw.circle(playSurface, white, (394, 274), 10),
     pygame.draw.circle(playSurface, white, (416, 274), 10),
     pygame.draw.circle(playSurface, white, (438, 274), 10),
     pygame.draw.circle(playSurface, white, (460, 274), 10),
     pygame.draw.circle(playSurface, red, (328, 350), 10),
     pygame.draw.circle(playSurface, red, (317, 331), 10),
     pygame.draw.circle(playSurface, red, (339, 331), 10),
     pygame.draw.circle(playSurface, red, (306, 312), 10),
     pygame.draw.circle(playSurface, red, (328, 312), 10),
     pygame.draw.circle(playSurface, red, (350, 312), 10),
     pygame.draw.circle(playSurface, red, (295, 293), 10),
     pygame.draw.circle(playSurface, red, (317, 293), 10),
     pygame.draw.circle(playSurface, red, (339, 293), 10),
     pygame.draw.circle(playSurface, red, (361, 293), 10),
     pygame.draw.circle(playSurface, grey, (383, 292), 10)
     ])


def desenhaTabuleiro():
    pass


print(bolas[0])

print(type(len(bolas)))


def getcolor():
    pass


getcolor()


def acertou(mouse):
    tamanho = int(len(bolas))
    i = 0
    for i in range(0, tamanho):
        quadrado_x = (mouse[0] - (bolas[i][0] + 10)) ** 2
        quadrado_y = (mouse[1] - (bolas[i][1] + 10)) ** 2

        if (math.sqrt(quadrado_x + quadrado_y) <= 10):
            # print("tu ta numa bola")
            cordopixel = playSurface.get_at(mouse)[:3]
            return cordopixel
        else:
            # print("tu num ta numa bola")
            pass
    return False


def pegando_se_tem_cor(mouse):
    everde = False
    evermelho = False
    ebranco = False
    if acertou(mouse) == (255, 0, 0):
        evermelho = (255, 0, 0)
        return evermelho
    elif acertou(mouse) == (0, 255, 0):
        everde = (0, 255, 0)
        return everde
    elif acertou(mouse) == (255, 255, 255):
        ebranco = (255, 255, 255)
        return ebranco
    else:
        return False


def coordenada_circulo(mouse):
    tamanho = int(len(bolas))
    i = 0
    lista = []
    for i in range(0, tamanho):
        quadrado_x = (mouse[0] - (bolas[i][0] + 10)) ** 2
        quadrado_y = (mouse[1] - (bolas[i][1] + 10)) ** 2

        if (math.sqrt(quadrado_x + quadrado_y) <= 10):
            # print("tu ta numa bola")
            return bolas[i]
        else:
            # print("tu num ta numa bola")
            pass
    return False


def mudaracor():
    if coordenada_circulo(mouse) is not None and pegando_se_tem_cor(mouse) is not (255, 255, 255):
        x = coordenada_circulo(mouse)[0]
        y = coordenada_circulo(mouse)[1]
        lista.append(x)
        lista.append(y)
        print(lista)
    else:
        pass
    # if len(lista) == 2:
    #     if lista[0] is not



def pegarvizinhancas():
    pass


pygame.display.set_caption("Chinese Checkers!")

while True:  # main game loop

    for event in pygame.event.get():
        # print(pygame.mouse.get_pos())

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONDOWN:
            mouse = event.pos
            print(mudaracor())
            print(pegando_se_tem_cor(mouse))
            print(coordenada_circulo(mouse))
            # print(coordenada_circulo(mouse)[0])

            print(acertou(mouse))
            mouseClicked = True

    pygame.display.update()

time.sleep(10)
