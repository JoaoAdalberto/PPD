import Pyro4
import sys
import threading
import AgoraVai

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class servidor():
    def __init__(self):
        self.lista_players = []
        self.jogador_atual = "verde"
        self.ganhador = "NENHUM"

    def get_jogador_atual(self):
        return self.jogador_atual

    def get_lista_players(self):
        return self.lista_players

    def set_ganhador(self, ganhador):
        self.ganhador = ganhador

    def get_ganhador(self):
        return self.ganhador

    def add_player(self, cliente):
        self.lista_players.append(cliente)
        if len(self.lista_players) == 2:
            self.print_to_all()
        print(self.lista_players)

    def pode_add_player(self):
        if (len(self.lista_players) < 2):
            return True
        else:
            return False

    def troca_jogador(self):
        if (self.jogador_atual == "vermelho"):
            self.jogador_atual = "verde"
        elif (self.jogador_atual == "verde"):
            self.jogador_atual = "vermelho"

    def adversario_add_mensagem_Chat(self, quem_mandou, mensagem):
        for player in self.lista_players:
            if player.get_my_username() != quem_mandou:
                print("Passou por aqui")
                player.add_mensagem_Chat(mensagem)

    def print_to_all(self):
        for player in self.lista_players:
            player.print()

    def adversario_att_tabuleiro(self, quem_mandou):
        for player in self.lista_players:
            if player.get_my_username() != quem_mandou:
                player.Att_tabuleiro()

    def adversario_troca_cor(self, peca_destino, peca_atual, quem_mandou):
        for player in self.lista_players:
            if player.get_my_username() != quem_mandou:
                player.troca_cor(peca_destino, peca_atual)

    def adversario_reset_tabuleiro(self, quem_mandou):
        for player in self.lista_players:
            if player.get_my_username() != quem_mandou:
                player.reset_tabuleiro()


def register_name_server_object():
    daemon = Pyro4.Daemon()
    uri = daemon.register(AgoraVai.cliente)
    ns = Pyro4.locateNS()
    ns.register("clientes", uri)
    print('Before Request Loop')
    threading.Thread(target=daemon.requestLoop).start()
    print('After Pyro4 Daemon')


def return_obj_name_server(uri):
    return Pyro4.Proxy(uri)


def main():
    daemon = Pyro4.Daemon()
    uri = daemon.register(servidor)
    ns = Pyro4.locateNS()
    ns.register("servidor", uri)
    print(uri)
    daemon.requestLoop()


if __name__ == "__main__":
    main()
