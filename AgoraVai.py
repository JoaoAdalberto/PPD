import sys
import os
import pygame
import math
import random
import numpy as np
from tabuleiro import Bola
from pygame.locals import *
from tkinter import *
from tkinter import ttk
from pygame import Surface

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
lista = [[], []]
listadecor = []
highlightcolor = blue
color = pygame.Color
pygame.init()
playSurface = pygame.display.set_mode(size)
playSurface.fill(grey)
mousex = 0
mousey = 0

bolas_selecionadas = []


# Grid



