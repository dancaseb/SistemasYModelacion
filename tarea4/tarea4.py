import numpy as np
import matplotlib.pyplot as plt
import random


distraction_probability = 0.6
iterations = 50
num_cars = 10
max_speed = 5
vector_length = 50


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
        if car_ahead_position < self.position:
            car_ahead_position += vector_length # continous road, car is not behind, but infront by road length
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
    def __init__(self, iterations, vector_length):
        self.matrix = np.ones((iterations, vector_length), dtype=int)
        self.matrix *= -1 # -1 will be empty spot, 0 is a car with speed 0
        random_positions = np.random.choice(vector_length, num_cars, replace=False)
        random_positions.sort()
        self.cars = [Car(np.random.randint(1, max_speed + 1), random_positions[i], distraction_probability, np.random.uniform(0,0.9,size=3)) for i in range(num_cars)]
        # self.matrix[0, [car.position for car in self.cars]] = [car.speed for car in self.cars] # initial state
        self.grid = np.ones((iterations, vector_length, 3)) # grid for plotting the cars
        # self.grid[0, [car.position for car in self.cars]] = [car.colour for car in self.cars]


    def simulate(self, step):
        for index, car in enumerate(self.cars):
            car_ahead_position = self.cars[(index + 1) % num_cars].position
            car.calculate_speed(car_ahead_position)
        self.matrix[step, [car.position for car in self.cars]] = [car.speed for car in self.cars] # initial state
        self.grid[step, [car.position for car in self.cars]] = [car.colour for car in self.cars]

        for car in self.cars:
            car.move()
        # self.matrix[step, [car.position for car in self.cars]] = [car.speed for car in self.cars] # update computational matrix
        # self.grid[step, [car.position for car in self.cars]] = [car.colour for car in self.cars] # update plotting matrix
    
    def plot_simulation(self):
        fig, ax = plt.subplots()
        ax.imshow(self.grid)
        for i, row in enumerate(self.matrix):
            for j, element in enumerate(row):
                if element != -1:
                    ax.text(j, i, f"{element}", va='center', ha='center', fontsize=12, color='black')
        ax.set_xticks(np.arange(vector_length + 1) - 0.5, minor=True)
        ax.set_yticks(np.arange(iterations + 1) - 0.5, minor=True)
        ax.grid(which="minor", color="black", linestyle='-', linewidth=1)

        plt.show()


s = Simulation(iterations, vector_length)
for step in range(0, iterations):
    s.simulate(step)
print(s.matrix)
s.plot_simulation()
