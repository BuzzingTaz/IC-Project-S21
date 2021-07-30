def get_frequencies(text):
    freq_arr = [0]*256
    for i in text:
        freq_arr[ord(i)] += 1

    
    counts_arr = []
    
    for char, count in enumerate(freq_arr):
        if(count):
            counts_arr.append((chr(char),count))
    
    return counts_arr
            

def print_frequencies(counts_arr):
    print("\nCharacters\t\t--> Frequencies")
    for char,count in counts_arr:
        print(f'\'{char}\' (ASCII = {ord(char)})\t-->  {str(count)}')
    