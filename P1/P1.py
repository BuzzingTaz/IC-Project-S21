freq_arr = [0]*256
with open("File_1.txt", "r") as file:
    text = file.read()
    for i in text:
        freq_arr[ord(i)] += 1

counts_arr = []
for char, count in enumerate(freq_arr):
    if(count):
        counts_arr.append((char,count))
        print(f'\'{chr(char)}\' -->  {str(count)}')


counts_arr.sort(reverse=True, key = lambda counts_arr: counts_arr[1])
