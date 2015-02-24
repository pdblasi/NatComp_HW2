from __future__ import print_function
import numpy as np
import math

class EA:
    bit_masks = ( 0b0000000000000001,
                  0b0000000000000010,
                  0b0000000000000100,
                  0b0000000000001000,
                  0b0000000000010000,
                  0b0000000000100000,
                  0b0000000001000000,
                  0b0000000010000000,
                  0b0000000100000000,
                  0b0000001000000000,
                  0b0000010000000000,
                  0b0000100000000000,
                  0b0001000000000000,
                  0b0010000000000000,
                  0b0100000000000000,
                  0b1000000000000000 )

    reproduction_masks = ( 0b1111111111111100,
                           0b1111111111111000,
                           0b1111111111110000,
                           0b1111111111100000,
                           0b1111111111000000,
                           0b1111111110000000,
                           0b1111111100000000,
                           0b1111111000000000,
                           0b1111110000000000,
                           0b1111100000000000,
                           0b1111000000000000,
                           0b1110000000000000,
                           0b1100000000000000 )

    binary_format = '{:#018b}'

    def __init__(self, population_size, mutation_rate):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = np.zeros(dtype=np.int16, shape=(self.population_size, 2))
        self.__next_population = np.zeros(dtype=np.int16, shape=(self.population_size, 2))
        self.__child_population = np.zeros(dtype=np.int16, shape=(math.ceil(self.population_size / 2), 2))

    def print_best(self):
        return

    def eval(self):
        return

if __name__ == '__main__':
    test = EA(1000, .01)
    print("hello world.")