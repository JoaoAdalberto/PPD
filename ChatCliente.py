def send(msg, client_socket):  # event is passed by binders.
    """Handles sending of messages."""
    msg = msg.encode("utf8")
    message_header = f"{len(msg):<{10}}".encode('utf-8')

    client_socket.send(message_header + msg)


def receive(client_socket):
    """Handles receiving of messages."""
    global msg
    username = client_socket.recv(BUFSIZ).decode("utf-8")
    while True:
        try:

            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(msg)
        except OSError:  # Possibly client has left the chat.
            break
    return username, msg

BUFSIZ = 1024
msg_list = []

# ----Now comes the sockets part----

