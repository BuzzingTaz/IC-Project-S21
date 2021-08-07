from math import log2
from math import ceil
import sys
import json
import time

import utils
import huffman



## Asking user input

file_number = input("Enter file number to be encoded: ")
operation = input("Enter operation E/D/B (Encode/Decode/Both): ")


## Reading file and setup

file_location = "./Inputs/File_" + file_number + ".txt"
text = open(file_location,"r").read()

# counts_arr contains a list of (char, freq) pairs
counts_arr = utils.get_frequencies(text)
utils.print_frequencies(counts_arr)


if (operation[0].lower() == 'e'or operation[0].lower() == 'b'):

    ## Generating Huffman code

    gen_time = time.time_ns()/1000000
    # Using a copy of counts_arr to generate huffman tree and code
    huff_tree = huffman.make_tree(counts_arr.copy())
    huffman_code = huffman.generate(huff_tree)
    gen_time = time.time_ns()/1000000 - gen_time

    print(f'Time to Generate Huffman Code: {gen_time}ms')


    # Saving huffman code to a json file for further use
    json.dump(huffman_code, open(f"Code{file_number}.json", 'w'))
    huffman.display(huffman_code)

    symbols = 0
    for (char, count) in counts_arr:
        symbols += count*len(huffman_code[char])

    print(f"Average length of Huffman encoded codeword: {symbols/len(text)}")
    print("\n=================\n")

    ## Encoding

    huffman_code = json.load(open(f"Code{file_number}.json", "r"))

    enc_time = time.time_ns()/1000000
    enc_string = huffman.encode(text, huffman_code)
    enc_time = time.time_ns()/1000000 - enc_time

    print(f'Time to Enncode text: {enc_time}ms')
    print(f"\nSize of text without encoding: {8*len(text)} bits")
    print(f"\nSize of text with fixed length code: {len(text)*ceil(log2(len(counts_arr)))} bits")
    print(f"\nSize of Huffman encoded string: {len(enc_string)} bits\n")

    open(f"./Results/Encoded_output{file_number}.txt", 'w').write(enc_string)
    print(f"The encoded sequence is in Results/Encoded_output{file_number}.txt")

    print("\n=================\n")


if(operation[0].lower() == 'd' or operation[0].lower() == 'b'):

    ## Decoding
    try:
        huffman_code = json.load(open(f"Code{file_number}.json", "r"))

        enc_output = open(f"./Results/Encoded_output{file_number}.txt", "r").read()
    except FileNotFoundError:
        print(f"No Encoded file was found.\nPlease run encoding for file {file_number} before decoding")
        print("Nothing was decoded")
        sys.exit()

    dec_time = time.time_ns()/1000000
    decoded_output = huffman.decode(enc_output, huffman_code)
    dec_time = time.time_ns()/1000000 - dec_time

    print(f'Time to Decode text: {dec_time}ms')

    open(f"./Results/Decoded_output{file_number}.txt", 'w').write(decoded_output)
    print(f"\nThe Decoded string is in Results/Decoded_output{file_number}.txt\n")

try:
    len(huffman_code)
except NameError:
    print("\nInvalid operation")