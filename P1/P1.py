from TreeNode import TreeNode
import huffman
from math import log2
from math import ceil
import json


freq_arr = [0]*256
with open("./Inputs/File_1.txt", "r") as file:
    text = file.read()
    for i in text:
        freq_arr[ord(i)] += 1

# counts_arr contains a list of (char, freq) integer pairs
counts_arr = []
print("Characters --> Frequencies")
for char, count in enumerate(freq_arr):
    if(count):
        counts_arr.append((char,count))
        print(f'\'{chr(char)}\' -->  {str(count)}')
print()

# Using a copy of counts_arr to generate huffman tree and code
huff_tree = huffman.make_tree(counts_arr.copy())
huffman_code = huffman.generate(huff_tree)

with open("Code.json", 'w') as f_json:
    json.dump(huffman_code, f_json)


symbols = 0
print("List of Huffman Codes:")
for (char, count) in counts_arr:
    print(f"\'{chr(char)}\' --> {huffman_code[char]}")
    symbols += count*len(huffman_code[char])

print(f"Average length of codeword = {symbols/len(text)}")


## Encoding

enc_string = huffman.encode(text, huffman_code)

with open("./Results/Encoded_output.txt", 'w') as file:
    file.write(enc_string)


print(f"size of text without encoding: {8*len(text)} bits")
print(f"Size of text with fixed length code: {len(text)*ceil(log2(len(counts_arr)))} bits")
print(f"Size of Huffman encoded string: {len(enc_string)} bits")


## Decoding

with open("./Results/Encoded_output.txt", "r") as file:
    enc_output = file.read()


decoded_output = huffman.decode(enc_output, huffman_code)


with open("./Results/Decoded_output.txt", 'w') as file:
    file.write(decoded_output)