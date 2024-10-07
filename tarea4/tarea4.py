import numpy as np
import matplotlib.pyplot as plt
import random
import sys

# Nagel-Schreckenberg algorithm. Necesarry to install numpy and matplotlib libraries
# execute -> python tarea4.py [distraction_probability] [iterations] [num_cars] [max_speed] [vector_length]
# max_speed and vector_length are optional parameters, default values are 5 and 50 respectively



class Car:
    def __init__(self, speed, position, distraction_probability, colour):
        self.speed = speed
        self.position = position
        self.distraction_probability = distraction_probability
        self.colour = colour
    
    def calculate_speed(self, car_ahead_position: int):
        # acceleration
        if self.speed < max_speed:
            self.speed += 1
        # slowing down
        if car_ahead_position <= self.position:
            car_ahead_position += vector_length # continous road, car ahead is not behind, but infront by road length
        distance_between_cars = car_ahead_position - self.position - 1 # if car at position 2 and car ahead at position 3, distance is zero
        if  distance_between_cars <= self.speed:
            self.speed = distance_between_cars

        # random slow down
        if self.speed >= 1 and random.random() < self.distraction_probability:
            self.speed -= 1
        
    def move(self):
        self.position += self.speed
        self.position %= vector_length

class Simulation:
    def __init__(self, iterations, vector_length, num_cars, max_speed, distraction_probability):
        self.speed_matrix = np.ones((iterations, vector_length), dtype=int)
        self.speed_matrix *= -1 # -1 will be empty spot, 0 is a car with speed 0
        random_positions = np.random.choice(vector_length, num_cars, replace=False)
        random_positions.sort()
        self.cars = [Car(np.random.randint(1, max_speed + 1), random_positions[i], distraction_probability, np.random.uniform(0,0.9,size=3)) for i in range(num_cars)]
        self.colour_matrix = np.ones((iterations, vector_length, 3)) # grid for plotting the cars


    def simulate(self, step):
        for index, car in enumerate(self.cars):
            car_ahead_position = self.cars[(index + 1) % num_cars].position
            car.calculate_speed(car_ahead_position)
        self.speed_matrix[step, [car.position for car in self.cars]] = [car.speed for car in self.cars] # update computational matrix
        self.colour_matrix[step, [car.position for car in self.cars]] = [car.colour for car in self.cars] # update plotting matrix

        for car in self.cars:
            car.move()
    
    def plot_simulation(self):
        fig, ax = plt.subplots()
        ax.imshow(self.colour_matrix)
        for i, row in enumerate(self.speed_matrix):
            for j, element in enumerate(row):
                if element != -1:
                    ax.text(j, i, f"{element}", va='center', ha='center', fontsize=12, color='black')
        ax.set_xticks(np.arange(vector_length + 1) - 0.5, minor=True)
        ax.set_yticks(np.arange(iterations + 1) - 0.5, minor=True)
        ax.grid(which="minor", color="black", linestyle='-', linewidth=1)

        plt.show()

if __name__ == "__main__":
    # parser options
    if len(sys.argv) < 4:
        print("ERROR! Run -> python tarea4.py [distraction_probability] [iterations] [num_cars] [max_speed] [vector_length]")
        sys.exit(1)
    distraction_probability = float(sys.argv[1])
    iterations = int(sys.argv[2])
    num_cars = int(sys.argv[3])
    max_speed = 5
    vector_length = 50
    if len(sys.argv) > 4:
        max_speed = int(sys.argv[4])
    if len(sys.argv) > 5:
        vector_length = int(sys.argv[5])


    s = Simulation(iterations, vector_length, num_cars, max_speed, distraction_probability)
    for step in range(0, iterations):
        s.simulate(step)
    s.plot_simulation()
