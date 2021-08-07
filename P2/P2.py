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

                if (c_estimate != cbar):
                    E += 1

            if (E < minE):
                minE = E

            print(f"The probability of error in decoding for trial {l} is equal to {E/N}")

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



# At k = 11, we are picking 2^11 codewords. ie, for n = 10, rate of code > 1 (since |C| = 2^nR, k = nR)
# so we get a higher than usual probability of error for k = 11 n = 10. (since rate is more than channel capacity)
# Channel capacity = 1-H2(p)
# 1-H2(0.015) = 0.8876
# 1-H2(0.1) = 0.5310
# 1-H2(0.45) = 0.0072

## Points for presentation
#
# Minimizing error by choosing proper codewords with distance np
