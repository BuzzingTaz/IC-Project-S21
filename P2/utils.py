from random import randint
from random import uniform


# Function to find the Hamming Distance between two strings
def HammingDistance(c1, c2):

    distance = 0

    for i in range(len(c1)):

        if c1[i] != c2[i]:
            distance += 1

    return distance


# Function to find the Minimum Hamming Distance between a string and the rest of the strings in the code
def MDD(ybar,code):

    minHammingDistance = 99999
    minset = [] # Set of all codewords in the code that have the minimum Hamming Distance compared to ybar

    for codeword in code:

        distance = HammingDistance(ybar,codeword)

        if distance < minHammingDistance:
            minHammingDistance = distance

    for codeword in code:

        dist = HammingDistance(ybar, codeword)

        if dist == minHammingDistance:
            minset.append(codeword)

    return minset

# Function to generate a code of size 2^k from the vector space {0,1}^k
def codegen(n,k):

    code = []

    for i in range(2**k):

        codeword = ''

        for j in range(n):

            codeword +=  str(randint(0,1))

        code.append(codeword)

    return code


# Bitflip function
def flip(bit):

    if bit == 0:
        return 1
    else:
        return 0

def BSC(p, cbar):
    ybar = ''
    for i in cbar:
        if uniform(0,1) <= p:
            ybar += str(flip(int(i))) # Flipping a bit with probability p

        else:
            ybar += str(i) # Not flipping a bit with probability 1-p

    return ybar