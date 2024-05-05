from Huffman import HuffmanEncoding, HuffmanDecoding


the_data = "Zażółć gęślą jaźń"
print(the_data)
encoding, the_tree = HuffmanEncoding(the_data)
print("\nEncoded output:")
print(encoding)
print("\nDecoded Output:")
print(HuffmanDecoding(encoding, the_tree))
