from Huffman import HuffmanEncoding, HuffmanDecoding
from FileManipulation import ReadFromFile

# the_data = "Zażółć gęślą jaźń"
# print(the_data)
encoding, the_tree = HuffmanEncoding(ReadFromFile())
print("\nEncoded output:")
print(encoding)
print("\nDecoded Output:")
print(HuffmanDecoding(encoding, the_tree))
