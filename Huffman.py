from Huffman_helpers import CalculateFrequency, CompressionShowcase, CalculateCodes, OutputEncoded
from NodesClass import Nodes


def HuffmanEncoding(the_data):
    symbolWithProbs = CalculateFrequency(the_data)
    the_symbols = symbolWithProbs.keys()
    the_frequencies = symbolWithProbs.values()
    print("symbols: ", the_symbols)
    print("frequencies: ", the_frequencies)

    the_nodes = []

    for symbol in the_symbols:
        the_nodes.append(Nodes(symbolWithProbs.get(symbol), symbol))

    while len(the_nodes) > 1:
        the_nodes = sorted(the_nodes, key=lambda x: x.frequency)

        right = the_nodes[0]
        left = the_nodes[1]

        left.code = 0
        right.code = 1

        newNode = Nodes(left.frequency + right.frequency, left.symbol + right.symbol, left, right)

        the_nodes.remove(left)
        the_nodes.remove(right)
        the_nodes.append(newNode)

    huffmanEncoding = CalculateCodes(the_nodes[0])
    print("symbols with codes", huffmanEncoding)
    CompressionShowcase(the_data, huffmanEncoding)
    encodedOutput = OutputEncoded(the_data, huffmanEncoding)
    return encodedOutput, the_nodes[0]


def HuffmanDecoding(encodedData, huffmanTree):
    treeHead = huffmanTree
    decodedOutput = []
    for x in encodedData:
        if x == "1":
            huffmanTree = huffmanTree.right
        elif x == "0":
            huffmanTree = huffmanTree.left
        try:
            if huffmanTree.left.symbol == None and huffmanTree.right.symbol == None:
                pass
        except AttributeError:
            decodedOutput.append(huffmanTree.symbol)
            huffmanTree = treeHead

    string = "".join([str(item) for item in decodedOutput])
    return string
