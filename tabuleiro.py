import pygame
import numpy as np
from bolas import Bola

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (128, 128, 128)


class Grid():
    def __init__(self):
        self.bolas = np.array([[Bola(green, 328, 46)],
                               [Bola(green, 317, 65), Bola(green, 339, 65)],
                               [Bola(green, 306, 84), Bola(green, 328, 84), Bola(green, 350, 84)],
                               [Bola(green, 295, 103), Bola(green, 317, 103), Bola(green, 339, 103),
                                Bola(green, 361, 103)],
                               [Bola(white, 207, 141), Bola(white, 229, 141), Bola(white, 251, 141),
                                Bola(white, 273, 141),
                                Bola(white, 295, 141),
                                Bola(white, 317, 141), Bola(white, 339, 141), Bola(white, 361, 141),
                                Bola(white, 383, 141),
                                Bola(white, 405, 141),
                                Bola(white, 427, 141), Bola(white, 449, 141), Bola(white, 218, 160)],
                               [Bola(white, 240, 160), Bola(white, 262, 160), Bola(white, 284, 160),
                                Bola(white, 306, 160),
                                Bola(white, 328, 160),
                                Bola(white, 350, 160), Bola(white, 372, 160), Bola(white, 394, 160),
                                Bola(white, 416, 160),
                                Bola(white, 438, 160),
                                Bola(white, 229, 179), Bola(white, 251, 179)],
                               [Bola(white, 273, 179), Bola(white, 295, 179), Bola(white, 317, 179),
                                Bola(white, 339, 179),
                                Bola(white, 361, 179),
                                Bola(white, 383, 179), Bola(white, 405, 179), Bola(white, 427, 179)],
                               [Bola(white, 240, 198), Bola(white, 262, 198), Bola(white, 284, 198),
                                Bola(white, 306, 198),
                                Bola(white, 328, 198),
                                Bola(white, 372, 198), Bola(white, 394, 198), Bola(white, 416, 198)],
                               [Bola(white, 229, 217), Bola(white, 251, 217), Bola(white, 273, 217),
                                Bola(white, 295, 217),
                                Bola(white, 317, 217),
                                Bola(white, 339, 217), Bola(white, 361, 217), Bola(white, 383, 217),
                                Bola(white, 405, 217),
                                Bola(white, 427, 217)],
                               [Bola(white, 218, 236), Bola(white, 240, 236), Bola(white, 262, 236),
                                Bola(white, 284, 236),
                                Bola(white, 306, 236),
                                Bola(white, 328, 236), Bola(white, 350, 236), Bola(white, 372, 236),
                                Bola(white, 394, 236),
                                Bola(white, 416, 236),
                                Bola(white, 438, 236)],
                               [Bola(white, 207, 255), Bola(white, 229, 255), Bola(white, 251, 255),
                                Bola(white, 273, 255),
                                Bola(white, 295, 255),
                                Bola(white, 317, 255), Bola(white, 339, 255), Bola(white, 361, 255),
                                Bola(white, 383, 255),
                                Bola(white, 405, 255),
                                Bola(white, 427, 255), Bola(white, 449, 255)],
                               [Bola(white, 196, 274), Bola(white, 218, 274), Bola(white, 240, 274),
                                Bola(white, 262, 274),
                                Bola(white, 284, 274),
                                Bola(white, 306, 274), Bola(white, 328, 274), Bola(white, 350, 274),
                                Bola(white, 372, 274),
                                Bola(white, 394, 274),
                                Bola(white, 416, 274), Bola(white, 438, 274), Bola(white, 460, 274)],
                               [Bola(red, 328, 350)],
                               [Bola(red, 317, 331), Bola(red, 339, 331)],
                               [Bola(red, 306, 312), Bola(red, 328, 312), Bola(red, 350, 312)],
                               [Bola(red, 295, 293), Bola(red, 317, 293), Bola(red, 339, 293), Bola(red, 361, 293)]])

    def desenha_estrela(self, screen):
        for array in self.bolas:
            for circulo in array:
                circulo.cria_bola(screen)
        pygame.display.flip()

    def verifica_dentro_do_circulo(self, x, y, a, b, r):
        return (x - a) * (x - a) + (y - b) * (y - b) < r * r

    def vizinhos(self, circulo):
        x = circulo.get_x()
        y = circulo.get_y()
        print(x, y)

    def pega_bola_na_posicao(self, x, y):
        for i, array in enumerate(self.bolas):
            for j, circulo in enumerate(array):
                a = Bola.get_x()
                b = Bola.get_y()
                if (a == x and b == y):
                    return circulo