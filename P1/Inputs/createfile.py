from math import ceil

with open("./File_1.txt", 'w') as f:
    str = "KEKW "
    for i in range(ceil(10240/len(str))):
        f.write(str)

