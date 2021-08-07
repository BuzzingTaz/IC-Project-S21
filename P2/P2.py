from random import choice

import matplotlib.pyplot as plt
import utils


# Defining relevant parameters
k = 10
n_array = range(15, 26)
p_array = [0.015, 0.1, 0.45]
PE_array = []

N = 2000  # Number of trials

print(f"The number of trials N = {N}")
print()

# Loop running over different values of p 
for p in p_array:

    temp_p_array = [] # Array to store PE for each n

    # Loop running over a sequence of n values
    for n in n_array:
        
        minE = float("inf")  # Minimum Error after performing 5 trials

        print(f"(n, k, p) = ({n}, {k}, {p})")

        for l in range(5):

            E = 0  # Number of errors made by the decoder

            code = utils.codegen(n, k)

            for j in range(N):

                # cbar is a randomly chosen codeword from the code
                cbar = choice(code)

                # ybar is the codeword after simulating the Binary Symmetric Channel
                ybar = utils.BSC(p, cbar)

                # Choosing any random codeword from the set of codewords with the minimum Hamming Distance
                c_estimate = choice(utils.MDD(ybar, code))

                # Checking if the decoder made an error
                if (c_estimate != cbar):
                    E += 1

            if (E < minE):
                minE = E

            print(f"The probability of error in decoding for trial {l+1} is equal to {E/N}")

        print(f"The minimum probability of error in decoding (after five trials) for this (n, k, p) tuple is {minE/N}.")
        print()
        temp_p_array.append(minE/N)

    PE_array.append(temp_p_array)


for i, pe in enumerate(PE_array):
    plt.plot(n_array, pe, marker='o', label=r"$p$ = "+f'{p_array[i]}')

plt.title(r"$P_E(n,k,p) = \frac{E}{N}$," + f" with k = {k}, N = {N}")
plt.xlabel(r"$n$")
plt.ylabel(r"$P_E(n,k,p)$")

plt.legend()
plt.show()


# Channel capacity = 1-H2(p)
# Following are the values of Channel capacity C for different values of p
#  
# 1) p = 0.015
#    C = 1-H2(0.015) = 0.8876
# 2) p - 0.1
#    C = 1-H2(0.1) = 0.5310
# 3) p = 0.45
#    C = 1-H2(0.45) = 0.0072
#

# Rate of code is defined as log|C|/n
# Where |C| is the number of codewords in code = 2^k
# and n is the length of each codeword
#
# So Rate, R = k/n

# 1) k = 10, n = (15,26)
# R ranges from 0.667 to 0.38
# In theory, Rate must be less than channel capacity to get a low probability of error
# This probability of error decreases exponentially as n increases as proved in class.
# This result is visible in the plots as well.
# For higher values of probability the channel capacity is much lesser and hence we need
# a longer code to have lesser error probability.


# 2) k = 11, n = (15,26)
# R ranges from 0.733 to 0.423
# The values of R is much higher in this case so we observe a higher error probability
# This error probability still reduces exponentially with n
#
# Also when a code is picked with 2^11 codewords of length < 11 will definitely 
# have duplicate codewords which add to the error probability

## Points for presentation
#
# Minimizing error by choosing proper codewords with distance np
