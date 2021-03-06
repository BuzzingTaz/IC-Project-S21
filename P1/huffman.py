from TreeNode import TreeNode

# Recursive function to find Huffman code given a tree
def generate(Node, enc_string = ''):

    if type(Node)==str:
        return{Node: enc_string}
    
    (left, right) = Node.children()
    enc_dict = {}
    enc_dict.update(generate(left, enc_string + '0'))
    enc_dict.update(generate(right, enc_string + '1'))

    return enc_dict


# Uses the huffman_code dictionary to lookup codeword and encodes input text
def encode(text, huffman_code):

    enc_string = ''
    for char in text:
        enc_string += huffman_code[char]
    
    return enc_string


# Reverses the huffman_code dictionary to use the codeword to find decoded text
def decode(text, huffman_code):

    decode_dict = {}
    decode_dict.update((code, char) for char,code in huffman_code.items())

    curr = ''
    output_string = ''

    for i in text:
        curr += i
        if curr in decode_dict:
            output_string+=decode_dict[curr]
            curr = ''
    
    return output_string


# Takes in array of (char, count) pairs and 
# iteratively creates a huffman tree
# The root node is returned
def make_tree(counts_arr):

    while len(counts_arr)>1:
        counts_arr.sort(reverse=True, key = lambda elem: elem[1])

        (elem1, freq1) = counts_arr.pop()
        (elem2, freq2) = counts_arr.pop()

        node = TreeNode(elem1, elem2)
        freq = freq1+freq2
        counts_arr.append((node,freq))
    
    return counts_arr[0][0]


# Displays the huffman code dictionary
def display(huffman_code):
    print("\nList of Huffman Codes:")
    for (char, code) in huffman_code.items():
        print(f"\'{char}\' (ASCII = {ord(char)})\t--> {code}")
        
        