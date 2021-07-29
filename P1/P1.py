from TreeNode import TreeNode
from huffman_generator import huffman_generator
from math import log2
from math import ceil

freq_arr = [0]*256
with open("File_1.txt", "r") as file:
    text = file.read()
    for i in text:
        freq_arr[ord(i)] += 1

# counts_arr contains a list of tuples with each tuple having character as first element and frequency as second
counts_arr = []
print("Characters --> Frequencies")
for char, count in enumerate(freq_arr):
    if(count):
        counts_arr.append((char,count))
        print(f'\'{chr(char)}\' -->  {str(count)}')


# Making a copy of counts_arr
huff_tree = counts_arr.copy()

while len(huff_tree)>1:
    huff_tree.sort(reverse=True, key = lambda elem: elem[1])

    (elem1, freq1) = huff_tree.pop()
    (elem2, freq2) = huff_tree.pop()

    node = TreeNode(elem1, elem2)
    freq = freq1+freq2
    huff_tree.append((node,freq))

huff_tree = huff_tree[0][0]
huffman_code = huffman_generator(huff_tree)


symbols = 0
print("List of Huffman Codes:")
for (char, count) in counts_arr:
    print(f"\'{chr(char)}\' --> {huffman_code[char]}")
    symbols += count*len(huffman_code[char])

print(f"Average length of codeword = {symbols/text.__len__()}")


## Encoding

enc_string = ''
for char in text:
    enc_string += huffman_code[ord(char)]

with open("Encoded_output.txt", 'w') as file:
    file.write(enc_string)

print(f"size of text without encoding: {8*len(text)} bits")
print(f"Size of text with fixed length code: {len(text)*ceil(log2(len(counts_arr)))} bits")
print(f"Size of Huffman encoded string: {len(enc_string)} bits")


## Decoding

with open("Encoded_output.txt", "r") as file:
    enc_output = file.read()
    
    
curr = ''
output_string = ''

decode_dict = dict()
decode_dict.update((code, char) for char,code in huffman_code.items())

for i in enc_output:
    curr += i
    if curr in decode_dict:
        output_string+=chr(decode_dict[curr])
        curr = ''

with open("Decoded_output", 'w') as file:
    file.write(output_string)