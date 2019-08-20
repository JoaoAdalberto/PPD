import sys
import os
import pygame
import math
import random
import numpy as np
from tabuleiro import Tabuleiro
from Botao import Botao
from caixadochat import CaixaChat
from textodeentrada import TextoEntrada
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
jogador_vermelho = "vermelho"
jogador_verde = "verde"
bolas_selecionadas = []
jogou_verde = 0
jogou_vermelho = 0
jogou = 0
jogador_atual = jogador_verde
botao_passar_turno = Botao("Passar a vez", (0, 0, 0), blue)
botao_passar_turno.desenha_botao(playSurface, 150, 450, 200, 50)

botao_desistir = Botao("Desistir", (255, 51, 255), blue)
botao_desistir.desenha_botao(playSurface, 150, 650, 200, 50)
caixa_chat = CaixaChat(playSurface, 500, 80, 600, 350, white)
texto_entrada = TextoEntrada(playSurface, 500, 460, 400, 110, white, "")

retangulodobotao = pygame.draw.rect(playSurface, (0, 0, 0), (150, 450, 200, 50))


def enviar_mensagem(input):
    texto_entrada.clean_input()
    pygame.display.flip()
    caixa_chat.adiciona_texto(0, input)
    caixa_chat.atualiza_tela_chatarray()

def mostra_jogador_atual(jogador_atual):
    while True:
        if jogador_atual == jogador_verde:
            pygame.draw.circle(playSurface, green, (100, 100), 20)
            break
        elif jogador_atual == jogador_vermelho:
            pygame.draw.circle(playSurface, red, (100, 100), 20)
            break


def troca_jogador_atual(jogador_atual):
    if jogador_atual == jogador_vermelho:
        jogador_atual = jogador_verde
    elif jogador_atual == jogador_verde:
        jogador_atual = jogador_vermelho
    return jogador_atual


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == MOUSE_LEFT:
                position_mouse = pygame.mouse.get_pos()

                if len(circulos) < 2:
                    position_mouse = pygame.mouse.get_pos()
                    x = position_mouse[0]
                    y = position_mouse[1]
                    circulo = tabuleiro.verifica_posicao_na_matriz(x, y)
                    if circulo is not None and jogador_atual == jogador_verde:
                        if circulo.get_cor() == (0, 255, 0):
                            circulos = []
                            # vizinhos=tabuleiro.pega_vizinhos(circulo)
                            circulos.append(circulo)
                        if circulo.get_cor() == white and len(circulos) > 0:
                            circulos.append(circulo)
                    elif circulo is not None and jogador_atual == jogador_vermelho:
                        if circulo.get_cor() == (255, 0, 0):
                            # vizinhos = tabuleiro.pega_vizinhos(circulo)
                            circulos.append(circulo)
                        if circulo.get_cor() == white and len(circulos) > 0:
                            circulos.append(circulo)
                if len(circulos) == 2:
                    tabuleiro.muda_posicao_circulo(circulos[0], circulos[1])
                    print(jogador_atual)
                    print(jogador_atual)
                    circulos = []
                if retangulodobotao.collidepoint(position_mouse):
                    if jogador_atual == jogador_vermelho:
                        jogador_atual = jogador_verde
                        pygame.draw.circle(playSurface, green, (100, 100), 20)
                        print(jogador_atual)
                    elif jogador_atual == jogador_verde:
                        jogador_atual = jogador_vermelho
                        pygame.draw.circle(playSurface, red, (100, 100), 20)
                        print(jogador_atual)
                tabuleiro.desenha_estrela(playSurface)
                tabuleiro.checa_se_tem_ganhador()

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
