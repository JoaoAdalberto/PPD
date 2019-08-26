def send(msg, client_socket):  # event is passed by binders.
    """Handles sending of messages."""
    msg = msg.encode("utf8")
    message_header = f"{len(msg):<{BUFSIZ}}".encode('utf-8')

    client_socket.send(message_header + msg)


def receive(client_socket):
    """Handles receiving of messages."""
    global msg
    username = client_socket.recv(BUFSIZ).decode("utf-8")
    msg = client_socket.recv(BUFSIZ).decode("utf8")
    msg_list.insert(msg)
    return username, msg

BUFSIZ = 1024
msg_list = []

# ----Now comes the sockets part----

