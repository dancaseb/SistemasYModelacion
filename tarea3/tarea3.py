import numpy as np
import matplotlib.pyplot as plt
import sys

# to run, it is necesarry to install numpy and matplotlib
# execute -> python tarea3.py [rule_number] [number of iterations] [vector length]
# e. g. python tarea3.py 60 15 100


if len(sys.argv) != 4:
    print("ERROR: You must pass 3 arguments to the script - rule number, number of iterations and vector length")
    sys.exit()

# parameters the user can modify
rule = int(sys.argv[1])
num_iterations = int(sys.argv[2])
vector_length = int(sys.argv[3])

rule_binary = f'{rule:08b}' # make rule a binary string (to be able to iterate through it)

simulation = np.zeros((num_iterations, vector_length), dtype=int)
simulation[0, vector_length // 2] = 1


for row in range(1, num_iterations):
    for col in range(vector_length):
        left_index = col-1
        middle_index = col
        right_index = col + 1
        if right_index >= vector_length:
            right_index = 0 # return to zero element of the row
        previous_generation = 2**2 * simulation[row-1,left_index] + 2**1 * simulation[row-1,middle_index] + 2**0 * simulation[row-1,right_index]
        if rule_binary[7 - previous_generation] == '1':
            simulation[row,col] = 1
        else:
            simulation[row,col] = 0

plt.imshow(simulation, cmap='Greys')
plt.show()