import pygame
import numpy as np
from bolas import Bola

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (128, 128, 128)


class Tabuleiro():
    def __init__(self):
        self.vizinhox = []
        self.bolas = np.array([Bola(green, 328, 46),
                               Bola(green, 317, 65), Bola(green, 339, 65),
                               Bola(green, 306, 84), Bola(green, 328, 84), Bola(green, 350, 84),
                               Bola(green, 295, 103), Bola(green, 317, 103), Bola(green, 339, 103),
                                Bola(green, 361, 103),
                               Bola(white, 196, 122), Bola(white, 218, 122), Bola(white, 240, 122), Bola(white, 262, 122),
                                Bola(white, 284, 122), Bola(white, 306, 122), Bola(white, 328, 122), Bola(white, 350, 122),
                                Bola(white, 372, 122), Bola(white, 394, 122), Bola(white, 416, 122), Bola(white, 438, 122),
                                Bola(white, 460, 122),
                               Bola(white, 207, 141), Bola(white, 229, 141), Bola(white, 251, 141),
                                Bola(white, 273, 141),
                                Bola(white, 295, 141),
                                Bola(white, 317, 141), Bola(white, 339, 141), Bola(white, 361, 141),
                                Bola(white, 383, 141),
                                Bola(white, 405, 141),
                                Bola(white, 427, 141), Bola(white, 449, 141),
                               Bola(white, 240, 160), Bola(white, 218, 160), Bola(white, 262, 160), Bola(white, 284, 160),
                                Bola(white, 306, 160),
                                Bola(white, 328, 160),
                                Bola(white, 350, 160), Bola(white, 372, 160), Bola(white, 394, 160),
                                Bola(white, 416, 160),
                                Bola(white, 438, 160),

                               Bola(white, 273, 179), Bola(white, 229, 179), Bola(white, 251, 179), Bola(white, 295, 179), Bola(white, 317, 179),
                                Bola(white, 339, 179),
                                Bola(white, 361, 179),
                                Bola(white, 383, 179), Bola(white, 405, 179), Bola(white, 427, 179),
                               Bola(white, 240, 198), Bola(white, 262, 198), Bola(white, 284, 198),
                                Bola(white, 306, 198),
                                Bola(white, 328, 198), Bola(white, 350, 198),
                                Bola(white, 372, 198), Bola(white, 394, 198), Bola(white, 416, 198),
                               Bola(white, 229, 217), Bola(white, 251, 217), Bola(white, 273, 217),
                                Bola(white, 295, 217),
                                Bola(white, 317, 217),
                                Bola(white, 339, 217), Bola(white, 361, 217), Bola(white, 383, 217),
                                Bola(white, 405, 217),
                                Bola(white, 427, 217),
                               Bola(white, 218, 236), Bola(white, 240, 236), Bola(white, 262, 236),
                                Bola(white, 284, 236),
                                Bola(white, 306, 236),
                                Bola(white, 328, 236), Bola(white, 350, 236), Bola(white, 372, 236),
                                Bola(white, 394, 236),
                                Bola(white, 416, 236),
                                Bola(white, 438, 236),
                               Bola(white, 207, 255), Bola(white, 229, 255), Bola(white, 251, 255),
                                Bola(white, 273, 255),
                                Bola(white, 295, 255),
                                Bola(white, 317, 255), Bola(white, 339, 255), Bola(white, 361, 255),
                                Bola(white, 383, 255),
                                Bola(white, 405, 255),
                                Bola(white, 427, 255), Bola(white, 449, 255),
                               Bola(white, 196, 274), Bola(white, 218, 274), Bola(white, 240, 274),
                                Bola(white, 262, 274),
                                Bola(white, 284, 274),
                                Bola(white, 306, 274), Bola(white, 328, 274), Bola(white, 350, 274),
                                Bola(white, 372, 274),
                                Bola(white, 394, 274),
                                Bola(white, 416, 274), Bola(white, 438, 274), Bola(white, 460, 274),
                               Bola(red, 328, 350),
                               Bola(red, 317, 331), Bola(red, 339, 331),
                               Bola(red, 306, 312), Bola(red, 328, 312), Bola(red, 350, 312),
                               Bola(red, 295, 293), Bola(red, 317, 293), Bola(red, 339, 293), Bola(red, 361, 293)])

    def desenha_estrela(self, screen):
        for circulo in self.bolas:
            circulo.cria_bola(screen)
        pygame.display.flip()

    def checa_se_tem_ganhador(self, playSurface):



        if self.bolas[0].get_cor() == (255, 0, 0) and self.bolas[1].get_cor() == (255, 0, 0) and self.bolas[2].get_cor() == (255, 0, 0) and self.bolas[3].get_cor() == (255, 0, 0) and self.bolas[4].get_cor() == (255, 0, 0) and self.bolas[5].get_cor() == (255, 0, 0) and self.bolas[6].get_cor() == (255, 0, 0) and self.bolas[7].get_cor() == (255, 0, 0) and self.bolas[8].get_cor() == (255, 0, 0) and self.bolas[9].get_cor() == (255, 0, 0):
            pygame.draw.circle(playSurface, red, (273, 179), 80)
            print("O VERMELHO GANHOUUUUUUUUUUUU UHULLLL")

        elif self.bolas[120].get_cor() == (0, 255, 0) and self.bolas[119].get_cor() == (0, 255, 0) and self.bolas[118].get_cor() == (0, 255, 0) and self.bolas[117].get_cor() == (0, 255, 0) and self.bolas[116].get_cor() == (0, 255, 0) and self.bolas[115].get_cor() == (0, 255, 0) and self.bolas[114].get_cor() == (0, 255, 0) and self.bolas[113].get_cor() == (0, 255, 0) and self.bolas[112].get_cor() == (0, 255, 0) and self.bolas[111].get_cor() == (0, 255, 0):
            pygame.draw.circle(playSurface, green, (273, 179), 80)
            print("O VERDE GANHOUUUUUUUUUUUU UHULLLL")




    def verifica_dentro_do_circulo(self, x, y, a, b, r):
        return (x - a) * (x - a) + (y - b) * (y - b) < r * r

    def pega_vizinhos(self, circulo):
        (x, y) = circulo.get_x_y()
        print(x, y)
        circulo_da_direita = self.pega_bola_na_posicao(x + 22, y)
        circulo_da_esquerda = self.pega_bola_na_posicao(x - 22, y)
        topo_circulo_esquerda = self.pega_bola_na_posicao(x - 11, y - 19)
        topo_circulo_direita = self.pega_bola_na_posicao(x + 11, y - 19)
        baixo_circulo_esquerda = self.pega_bola_na_posicao(x - 11, y + 19)
        baixo_circulo_direita = self.pega_bola_na_posicao(x + 11, y + 19)

        vizinhos = circulo_da_direita, circulo_da_esquerda, topo_circulo_direita, topo_circulo_esquerda, baixo_circulo_direita, baixo_circulo_esquerda
        bolas = []
        for vizinho in vizinhos:
            if vizinho is not None:
                bolas.append(vizinho)

        espacos_brancos = self.vizinhos_brancos(bolas)

        for w in espacos_brancos:
            bolas.append(w)
        if len(bolas) >= 0:
            inimigos_vizinhanca = self.inimigos_na_vizinhanca(circulo, bolas)
        if len(inimigos_vizinhanca) >= 0:
            for inimigo in inimigos_vizinhanca:
                if inimigo.moveu:
                    espacos_brancos = self.espacos_disponiveis(inimigo)
                    for brancos in espacos_brancos:
                        bolas.append(brancos)
        return bolas

    def espacos_disponiveis(self, inimigo):
        (x, y) = inimigo.get_x_y()
        circulo_da_direita = self.pega_bola_na_posicao(x + 22, y)
        circulo_da_esquerda = self.pega_bola_na_posicao(x - 22, y)
        topo_circulo_esquerda = self.pega_bola_na_posicao(x - 11, y - 19)
        topo_circulo_direita = self.pega_bola_na_posicao(x + 11, y - 19)
        baixo_circulo_esquerda = self.pega_bola_na_posicao(x - 11, y + 19)
        baixo_circulo_direita = self.pega_bola_na_posicao(x + 11, y + 19)

        vizinhos = circulo_da_direita, circulo_da_esquerda, topo_circulo_direita, topo_circulo_esquerda, baixo_circulo_direita, baixo_circulo_esquerda

        vizinhanca_filtrada = []
        for vizinho in vizinhos:
            if vizinho is not None:
                vizinhanca_filtrada.append(vizinho)

        espacos_brancos = self.vizinhos_brancos(vizinhanca_filtrada)

        return espacos_brancos

    def inimigos_na_vizinhanca(self, circulo, vizinhos):
        inimigos = []
        for vizinho in vizinhos:
            if self.verifica_se_vizinho_nao_e_branco(circulo, vizinho):
                inimigos.append(vizinho)
        return inimigos

    def vizinhos_brancos(self, vizinhos):
        brancos = []
        for vizinho in vizinhos:
            if vizinho is not None:
                if vizinho.get_cor() == white:
                    brancos.append(vizinho)
        return brancos

    def pega_bola_na_posicao(self, x, y):
        for i, array in enumerate(self.bolas):
            for j, circulo in enumerate(array):
                (a, b) = circulo.get_x_y()
                if (a == x and b == y):
                    return circulo

    # def pega_bola_na_posicao(self, x, y, jogador_atual):
    #     for i, array in enumerate(self.bolas):
    #         for j, circulo in enumerate(array):
    #             if jogador_atual == 0 and circulo.get_cor == green:
    #                 (a, b) = circulo.get_x_y()
    #                 if (a == x and b == y):
    #                     return circulo
    #             elif jogador_atual == 1 and circulo.get_cor == red:
    #                 (a, b) = circulo.get_x_y()
    #                 if (a == x and b == y):
    #                     return circulo

    def verifica_posicao_na_matriz(self, x, y):
        for circulo in self.bolas:
            (a, b) = circulo.get_x_y()
            if self.verifica_dentro_do_circulo(x, y, a, b, 10) and circulo.valido:
                return circulo

    def verifica_se_vizinho_nao_e_branco(self, circulo: Bola, vizinho_circulo: Bola):
        if vizinho_circulo is not None and vizinho_circulo.get_cor() != white:
            return True
        else:
            return False

    def muda_posicao_circulo(self, circulo, outro_circulo):
         # vizinhos_do_primeiro = self.pega_vizinhos(circulo)
        # for vizinho in vizinhos_do_primeiro:
        #     if vizinho.get_cor != (255, 255, 255):
        #         vizinhos_do_vizinhos = vizinho.get_x_y
        if outro_circulo.get_cor() == white:
                print(str(self.bolas[0].get_cor()) + " Pos: " + str(self.bolas[0].get_x_y()))
                print(str(self.bolas[10].get_cor()) + " Pos: " + str(self.bolas[10].get_x_y()))
                cor = (circulo.get_cor())
                circulo.set_cor(outro_circulo.get_cor())
                circulo.moveu = True
                outro_circulo.set_cor(cor)
                print(str(self.bolas[0].get_cor()) + " Pos: " + str(self.bolas[0].get_x_y()))
                print(str(self.bolas[10].get_cor()) + " Pos: " + str(self.bolas[10].get_x_y()))

    def troca_jogador_atual(self, jogador_atual):
        if jogador_atual == "vermelho":
            jogador_atual = "verde"
            return jogador_atual
        elif jogador_atual == "verde" :
            jogador_atual = "vermelho"
            return jogador_atual