# Recursive function to find Huffman code given a tree
def huffman_generator(Node, enc_string = ''):
    if type(Node)==int:
        return{Node: enc_string}
    
    (left, right) = Node.children()
    enc_dict = dict()
    enc_dict.update(huffman_generator(left, enc_string+'0'))
    enc_dict.update(huffman_generator(right, enc_string+'1'))

    return enc_dict