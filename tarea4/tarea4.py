import numpy as np

distraction_probability = 0.1
iterations = 5
num_cars = 4
max_speed = 5
vector_length = 15


class Car:
    def __init__(self, speed, position, distraction_probability):
        self.speed = speed
        self.position = position
        self.distraction_probability = distraction_probability
    
    def move(self, car_ahead_position: int):
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

        # move
        self.position += self.speed
        self.position %= vector_length

class Simulation:
    def __init__(self, iterations, vector_length):
        self.matrix = np.zeros((iterations, vector_length), dtype=int)
        random_positions = np.random.choice(vector_length, num_cars, replace=False)
        random_positions.sort()
        self.cars = [Car(np.random.randint(1, max_speed + 1), random_positions[i], distraction_probability) for i in range(num_cars)]
        self.matrix[0, [car.position for car in self.cars]] = [car.speed for car in self.cars] # initial state

    def simulate(self, step):
        for index, car in enumerate(self.cars):
            car_ahead_position = self.cars[(index + 1) % num_cars].position
            car.move(car_ahead_position)
        self.matrix[step, [car.position for car in self.cars]] = [car.speed for car in self.cars]

        


# 
s = Simulation(iterations, vector_length)
for step in range(1, iterations):
    s.simulate(step)
print(s.matrix)
# print (simulation)