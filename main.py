from Huffman import HuffmanEncoding, HuffmanDecoding
from FileManipulation import ReadFromFile, SaveToFile
from Sockets import Client, Server
import argparse
import pickle


def main():
    parser = argparse.ArgumentParser(description="Wybierz tryb: 'server' lub 'client'.")
    parser.add_argument("mode", choices=["server", "client"], help="Tryb pracy: 'server' lub 'client'.")
    args = parser.parse_args()

    if args.mode == "server":
        encoding, the_tree = HuffmanEncoding(ReadFromFile(input("Wczytaj plik (.txt): ")))
        Server(encoding, the_tree)
    elif args.mode == "client":
        message, key = Client()
        SaveToFile(input("\nZapisz plik (.txt): "), HuffmanDecoding(message, key))


if __name__ == "__main__":
    main()
