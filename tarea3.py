import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# parameters the user can modify
rule = 91
num_iterations = 15
vector_length = 70

rule_binary = f'{rule:08b}'

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
        if rule_binary[7 - previous_generation] == '1': # the index in the binary string is inverted
            simulation[row,col] = 1
        else:
            simulation[row,col] = 0

plt.imshow(simulation, cmap='Greys')
plt.show()