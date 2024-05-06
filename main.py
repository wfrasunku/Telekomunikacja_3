from huffman_algorithm import HuffmanEncoding, HuffmanDecoding
from file_manipulation import ReadFromFile, SaveToFile
from sockets import Client, Server
import argparse


def main():
    parser = argparse.ArgumentParser(description="arg[1] - 'server/client' arg[2] - 'path of file'")
    parser.add_argument("mode", choices=["server", "client"], help="'server' - sending, 'client' - receiving")
    parser.add_argument("path", help="path of saved/received file")
    args = parser.parse_args()

    if args.mode == "server":
        encoding, the_tree = HuffmanEncoding(ReadFromFile(args.path))
        Server(encoding, the_tree, input("Podaj adres hosta: "), int(input("Podaj numer portu: ")))
    elif args.mode == "client":
        try:
            message, key = Client(input("Podaj adres hosta: "), int(input("Podaj numer portu: ")))
        except Exception as e:
            print(e)
        SaveToFile(args.path, HuffmanDecoding(message, key))


if __name__ == "__main__":
    main()
