from random import choice

import matplotlib.pyplot as plt
import utils


# Defining relevant parameters
k = 10
n_array = range(15,26)
p_array = [0.015,0.1,0.45]
PE_array = []

N = 2000 # Number of trials

print(f"The number of trials N = {N}")
print()

for p in p_array:

    temp_p_array = []

    for n in n_array:

        minE = float("inf") # Minimum Error after performing 5 trials

        print(f"(n, k, p) = ({n}, {k}, {p})")

        for l in range(5):

            E = 0 # Number of errors made by the decoder

            code = utils.codegen(n,k)

            for j in range(N):

                cbar = choice(code) # cbar is a randomly chosen codeword from the code
                
                ybar = utils.BSC(p,cbar) # ybar is the codeword after simulating the Binary Symmetric Channel

                c_estimate = choice(utils.MDD(ybar,code)) # Choosing any random codeword from the set of codewords with the minimum Hamming Distance

                if (c_estimate != cbar):
                    E += 1

            if (E < minE):
                minE = E

            print(f"The probability of error in decoding for trial {l} is equal to {E/N}")

        print(f"The minimum probability of error in decoding (after five trials) for this (n, k, p) tuple is {minE/N}.")
        print()
        temp_p_array.append(minE/N)
    
    PE_array.append(temp_p_array)


for i,pe in enumerate(PE_array):
    plt.plot(n_array, pe, marker = 'o', label = r"$p$ = "+f'{p_array[i]}')

plt.title(r"$P_E(n,k,p) = \frac{E}{N}$," + f" with k = {k}, N = {N}")
plt.xlabel(r"$n$")
plt.ylabel(r"$P_E(n,k,p)$")

plt.legend()
plt.show()