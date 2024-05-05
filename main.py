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

        print("Struktura drzewa:")
        print_tree(the_tree)

        print("\nEncoded output:")
        print(encoding)

        print("\nTree output:")
        # Serializacja obiektu do postaci bajtowej
        serialized_node = pickle.dumps(the_tree)

        # Konwersja na bajty
        bytes_node = bytes(serialized_node)

        print("Converted node to bytes:", bytes_node)

        Server(encoding, the_tree)
    elif args.mode == "client":
        message, key = Client()
        print(message)
        print(key)
        text = HuffmanDecoding(message, key)
        SaveToFile(input("\nZapisz plik (.txt): "), text)

    # encoding, the_tree = HuffmanEncoding(ReadFromFile(input("Wczytaj plik (.txt): ")))
    # size = sys.getsizeof(the_tree)
    #
    # print("Size of the node object:", size * 8, "bits")
    # print("\nEncoded output:")
    # print(encoding)
    #
    # print("\nTree output:")
    # print(the_tree)
    # # SaveToFile("EncodedOutput.txt", encoding)
    # print("\nDecoded Output:")
    # print(HuffmanDecoding(encoding, the_tree))
    # SaveToFile(input("\nZapisz plik (.txt): "), HuffmanDecoding(encoding, the_tree))


if __name__ == "__main__":
    main()


def print_tree(node, level=0):
    if node is not None:
        print("  " * level + f"Symbol: {node.symbol}, Frequency: {node.frequency}, Code: {node.code}")
        print_tree(node.left, level + 1)
        print_tree(node.right, level + 1)
