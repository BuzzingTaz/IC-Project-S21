from random import uniform
from random import randint
from random import choice

# Bitflip function
def flip(bit):

    if bit == 0:
        return 1
    else:
        return 0


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


# Defining relevant parameters
tuples = [(15,10,0.015), (15,10,0.1), (15,10,0.45), (20,10,0.015), (20,10,0.1), (20,10,0.45)]
N = 2000 # Number of trials

print(f"The number of trials N = {N}")
print()

for n,k,p in tuples:

    minE = float("inf") # Minimum Error after performing 5 trials

    print(f"Tuple = ({n},{k},{p})")

    for l in range(5):

        E = 0 # Number of errors made by the decoder

        code = codegen(n,k)

        for j in range(N):

            ybar = '' # ybar is the codeword after simulating the Binary Symmetric Channel
            cbar = choice(code) # cbar is a randomly chosen codeword from the code

            for i in cbar:

                if uniform(0,1) <= p:
                    ybar += str(flip(int(i))) # Flipping a bit with probability p

                else:
                    ybar += str(i) # Not flipping a bit with probability 1-p

            c_estimate = choice(MDD(ybar,code)) # Choosing any random codeword from the set of codewords with the minimum Hamming Distance

            if (c_estimate != cbar):
                E += 1

        if (E < minE):
            minE = E

        print(f"The probability of error in decoding is equal to {E/N}")

    print(f"The minimum probability of error in decoding (after five trials) for this tuple is {minE/N}.")
    print()