from Huffman import HuffmanEncoding, HuffmanDecoding
from FileManipulation import ReadFromFile, SaveToFile


encoding, the_tree = HuffmanEncoding(ReadFromFile(input("Wczytaj plik (.txt): ")))
# print("\nEncoded output:")
# print(encoding)
SaveToFile("EncodedOutput.txt", encoding)
# print("\nDecoded Output:")
# print(HuffmanDecoding(encoding, the_tree))
SaveToFile(input("\nZapisz plik (.txt): "), HuffmanDecoding(encoding, the_tree))
