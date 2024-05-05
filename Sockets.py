import socket
import pickle


def Server(encoding, the_tree):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 2137))
    s.listen(5)

    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    data_to_send = {"encoded_message": encoding, "tree": the_tree}
    serialized_data = pickle.dumps(data_to_send)
    bytes_node = bytes(serialized_data)

    clientsocket.sendall(bytes_node)
    clientsocket.close()


def Client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 2137))

    received_data = b""
    while True:
        data = s.recv(4096)
        if not data:
            break
        received_data += data

    unpacked_data = pickle.loads(received_data)
    encoded_message = unpacked_data["encoded_message"]
    tree = unpacked_data["tree"]

    return encoded_message, tree
