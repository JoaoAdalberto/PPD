import pygame

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (128, 128, 128)


class CaixaChat:
    def __init__(self, playSurface, x, y, largura, altura, cor):
        self.playSurface = playSurface
        self.largura = largura
        self.rect = pygame.draw.rect(playSurface, cor, (x, y, largura, altura))
        pygame.display.flip()
        self.font = pygame.font.SysFont("Corbel", 20)
        self.chatarray = []
        self.texts = []

    def adiciona_texto(self, jogador_atual, texto):
        if len(self.chatarray) == 11:
            self.chatarray.pop(0)

        self.chatarray.append((jogador_atual, texto))

    def pega_todos_textos(self):
        return self.chatarray

    def reseta_interface(self):
        self.playSurface.fill(white)

    def atualiza_tela_chatarray(self):
        for index, value in enumerate(self.chatarray):
            jogador_atual, texto = value
            if jogador_atual == "verde":
                texto = (f"Jogador verde: {texto}")
                render_font = self.font.render(texto, True, green)
                pygame.draw.rect(self.playSurface, white, (500, 90 + (30 * index), self.largura, 30))
                self.playSurface.blit(render_font, (510, 90 + (30 * index)))
                pygame.display.flip()
            else:
                texto = (f"Jogador vermelho: {texto}")
                render_font = self.font.render(texto, True, red)
                pygame.draw.rect(self.playSurface, white, (500, 90 + (30 * index), self.largura, 30))
                self.playSurface.blit(render_font, (510, 90 + (30 * index)))
                pygame.display.flip()
