import socket
import pickle


def Server(encoding, the_tree):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip_address = socket.gethostbyname(socket.gethostname())
    print(f"Host Address: {ip_address}")
    s.bind((socket.gethostname(), int(input("Insert port number: "))))
    print("Waiting for connection...")
    s.settimeout(30)
    s.listen(1)

    try:
        clientsocket, address = s.accept()
    except socket.timeout:
        print("Connection timed out!")
        s.close()
        return

    print(f"Connected with {address}!")

    data_to_send = {"encoded_message": encoding, "tree": the_tree}
    serialized_data = pickle.dumps(data_to_send)
    bytes_node = bytes(serialized_data)

    clientsocket.sendall(bytes_node)
    clientsocket.close()
    print("File sent!")


def Client(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        print("Connected with server!")
    except ConnectionRefusedError:
        raise Exception("Cannot connect with server!")

    received_data = b""
    while True:
        data = s.recv(4096)
        if not data:
            break
        received_data += data

    unpacked_data = pickle.loads(received_data)
    encoded_message = unpacked_data["encoded_message"]
    tree = unpacked_data["tree"]
    print("File Received!")

    return encoded_message, tree
