import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

rule = 252
rule_binary = f'{rule:08b}'
num_iterations = 30
vector_length = 30

simulation = np.zeros((num_iterations, vector_length), dtype=int)
# simulation = np.random.randint(50, size=(num_iterations, vector_length))
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
print(simulation)

plt.imshow(simulation, cmap='Greys')
plt.show()