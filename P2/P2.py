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
    outputstr = ''

    for codeword in code:
        
        distance = HammingDistance(ybar,codeword)
        
        if distance < minHammingDistance:
            minHammingDistance = distance
            outputstr = codeword
    
    return outputstr

# Defining relevant parameters
codeword = ''
code = []
# tuples = [(15,10,0.015), (15,10,0.1), (15,10,0.45), (20,10,0.015), (20,10,0.1), (20,10,0.45)]
n = 15
k = 10
p = 0.015

for i in range(2^k):
    for j in range(n): 
        codeword +=  str(randint(0,1))

    code.append(codeword)
    codeword = ''

ybar = '' # ybar is the codeword after simulating the Binary Symmetric Channel
cbar = '' # cbar is a randomly chosen codeword from the code
E = 0 # Total Number of errors made in decoding
N = 2000 # Number of trials

for k in range(N):
    
    ybar = ''
    cbar = choice(code)
    
    for i in cbar:
        if uniform(0,1) <= p:
            ybar += str(flip(int(i))) # Flipping a bit with probability p

        else:
            ybar += str(i) # Not flipping a bit with probability 1-p
    
    c_estimate = MDD(ybar,code)

    if (c_estimate != cbar):
        E += 1  

print(f"The probability of error in decoding is equal to {E}")        
