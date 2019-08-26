import sys
import os
import pygame
import time
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tabuleiro import Tabuleiro
from Botao import Botao
from caixadochat import CaixaChat
from textodeentrada import TextoEntrada
from ChatCliente import *
from tkinter import *
from tkinter import ttk
from pygame import Surface

HEADER_LENGTH = 10


def send(message, client_socket):
    message = message.encode('utf-8')
    message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
    client_socket.send(message_header + message)


def receive(client_socket):
    username_header = client_socket.recv(HEADER_LENGTH)

    # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
    if not len(username_header):
        print('Connection closed by the server')
        sys.exit()

    # Convert header to int value
    username_length = int(username_header.decode('utf-8').strip())

    # Receive and decode username
    username = client_socket.recv(username_length).decode('utf-8')

    # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
    message_header = client_socket.recv(HEADER_LENGTH)
    message_length = int(message_header.decode('utf-8').strip())
    message = client_socket.recv(message_length).decode('utf-8')
    return (username, message)


# Parte do socket
HOST = input("Qual seu ip?")
PORT = 33000
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
# client_socket.settimeout(4)
name = input("Digite o seu nome:")
client_socket.send(name.encode("utf-8"))

msg1 = client_socket.recv(1024).decode("utf-8")
print(msg1)
# try:
msg2 = client_socket.recv(1024).decode("utf-8")
print(msg2)
# try:
#     msg3 = client_socket.recv(1024).decode("utf-8")
#
# except:
#     pass

# except Exception as e:
#     print(e)

# print(msg2)
# Global Variables
# inicializando o tamanho da tela e as cores q irei usar
FPS = 30
circulos = []
windowwidth = 1200
windowheight = 800
size = (windowwidth, windowheight)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (128, 128, 128)
MOUSE_LEFT = 1
MOUSE_RIGHT = 3

# inicializando o pygame e a tela
pygame.init()
playSurface = pygame.display.set_mode(size)
playSurface.fill(grey)
pygame.display.set_caption("Chinese Checkers")
tabuleiro = Tabuleiro()
tabuleiro.desenha_estrela(playSurface)

jogador_vermelho = "vermelho"
jogador_verde = "verde"
# setando p sempre o jogador verde comecar

jogador_atual = jogador_verde

# inicializando o botao de passar turno
botao_passar_turno = Botao("Passar a vez", (0, 0, 0), blue)
botao_passar_turno.desenha_botao(playSurface, 150, 450, 200, 50)
# inicializando o botao de enviar mensagens
send_mensage_button = Botao("Enviar", (255, 1, 127), white)
send_message_button_rect = send_mensage_button.desenha_botao(playSurface, 920, 490, 200, 50)
# inicializando o botao de desistir , mas nao ta funcionando ainda
botao_desistir = Botao("Desistir", (255, 51, 255), blue)
botao_desistir.desenha_botao(playSurface, 150, 650, 200, 50)
# inicializando a caixa do chat
caixa_chat = CaixaChat(playSurface, 500, 80, 600, 350, white)
# inicializando a caixa de entrada de texto
texto_entrada = TextoEntrada(playSurface, 500, 460, 400, 110, white, "")
retangulodobotao = pygame.draw.rect(playSurface, (0, 0, 0), (150, 450, 200, 50))
input_para_caixa_do_chat = ""


# codigo pra mostar jogador atual, so a mensagem sem nenhum botao perto
def message_display(x, y, text, size, cor):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText, cor)
    TextRect.center = (x, y)
    pygame.display.get_surface().blit(TextSurf, TextRect)


def text_objects(text, font, cor):
    textSurface = font.render(text, True, cor)
    return textSurface, textSurface.get_rect()


# desenhando o jogador atual e a bolinha que diz de quem e o turno
pygame.draw.circle(playSurface, green, (210, 40), 20)
message_display(100, 40, "Turno do jogador: ", 20, (0, 0, 0, 255))
pygame.display.flip()


# funcao para enviar mensagem, ta funcionando mas la no caixadochat tem que ajeitar
def enviar_mensagem(input, jogador_atual):
    texto_entrada.clean_input()
    pygame.display.flip()
    caixa_chat.adiciona_texto(jogador_atual, input)
    caixa_chat.atualiza_tela_chatarray(jogador_atual)


# mostra a bola do jogador atual
def mostra_jogador_atual(jogador_atual):
    while True:
        if jogador_atual == jogador_verde:
            pygame.draw.circle(playSurface, green, (120, 40), 20)
            break
        elif jogador_atual == jogador_vermelho:
            pygame.draw.circle(playSurface, red, (120, 40), 20)
            break


# troca o jogador atual
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
                # SE CLICAR NO ESPACO PRA DIGITAR, COMECA A DIGITACAO
                if texto_entrada.get_input_text_rect().collidepoint(event.pos):
                    texto_entrada.handle_event(event)
                # SE CLICAR NO BOTAO DE ENVIAR MENSAGEM ENVIA A MENSAGEM PRA CAIXA DO CHAT
                if send_message_button_rect.collidepoint(event.pos):
                    enviar_mensagem(input_para_caixa_do_chat, jogador_atual)
                position_mouse = pygame.mouse.get_pos()
                # LOGICA PRA TROCAR AS BOLAS
                if len(circulos) < 2:
                    position_mouse = pygame.mouse.get_pos()
                    x = position_mouse[0]
                    y = position_mouse[1]
                    circulo = tabuleiro.verifica_posicao_na_matriz(x, y)
                    if circulo is not None and jogador_atual == jogador_verde:
                        if circulo.get_cor() == (0, 255, 0):
                            circulos = []
                            circulos.append(circulo)
                        if circulo.get_cor() == white and len(circulos) > 0:
                            circulos.append(circulo)
                    elif circulo is not None and jogador_atual == jogador_vermelho:
                        if circulo.get_cor() == (255, 0, 0):
                            circulos.append(circulo)
                        if circulo.get_cor() == white and len(circulos) > 0:
                            circulos.append(circulo)
                if len(circulos) == 2:
                    tabuleiro.muda_posicao_circulo(circulos[0], circulos[1])
                    circulos = []
                tabuleiro.checa_se_tem_ganhador(playSurface)

                # Se clicar pra passar o turno troca os jogadores e muda a bola que diz de quem é o turno
                if retangulodobotao.collidepoint(position_mouse):
                    if jogador_atual == jogador_vermelho:
                        jogador_atual = jogador_verde
                        pygame.draw.circle(playSurface, green, (210, 40), 20)
                    elif jogador_atual == jogador_verde:
                        jogador_atual = jogador_vermelho
                        pygame.draw.circle(playSurface, red, (210, 40), 20)
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
        # Se apertar qualquer tecla aparece no espaco para digitar
        if event.type == pygame.KEYDOWN:
            texto_entrada.handle_event(event)
            input_para_caixa_do_chat = texto_entrada.draw(playSurface)
            pygame.display.flip()
