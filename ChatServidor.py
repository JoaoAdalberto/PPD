#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print(str(client_address) + " has connected.")
        # client.send(bytes("Bem vindo ao jogo, introduza seu nome!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s!' % name
    print(welcome)
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    clients[client] = name
    broadcast(msg)

    while True:
        msg = client.recv(BUFSIZ)
        broadcast(msg)


def broadcast(msg):  # prefix is for name identification
    """Broadcasts a message to all the clients."""

    for sock in clients:
        string = clients[sock] + " " + msg
        sock.send(string.encode("utf-8"))


clients = {}
addresses = {}

HOST = "127.0.0.1"
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(2)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
