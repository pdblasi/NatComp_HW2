from __future__ import print_function
import numpy as np
import math
import random

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
        self.child_population_size = self.population_size // 2
        self.mutation_rate = mutation_rate
        self.population = np.random.random_integers(0, 65535, self.population_size).astype(np.uint16)
        self.population_eval = np.zeros(dtype=np.float, shape=(self.population_size))
        self.__next_population = np.zeros(dtype=np.uint16, shape=(self.population_size  + self.child_population_size))
        self.__next_population_eval = np.zeros(dtype=np.float, shape=(self.population_size + self.child_population_size))
        self.__child_population = np.zeros(dtype=np.uint16, shape=(self.child_population_size))
        self.__child_population_eval = np.zeros(dtype=np.float, shape=(self.child_population_size))
        self.__child_pop_indices = range(self.child_population_size)
        self.__pop_indices = range(self.population_size)

        self.evaluate(self.population, self.population_eval);

    def print_best(self):
        index = 0
        max = 0
        for i in self.__pop_indices:
            if self.population_eval[i] > max:
                max = self.population_eval[i]
                index = i
        print(self.binary_format.format(self.population[index]), "\nX:", np.float32(self.population[index]) / 65535, "Y:", max, "\n")

    def evaluate(self, pop, eval):
        for i in range(pop.size):
            x = np.float32(pop[i]) / 65535
            eval[i] = (2 ** (-2 * (((x - 0.1)/.9) * ((x - 0.1)/.9))) * math.sin(5 * math.pi * x) ** 6)

    def select_indices(self, count, eval):
        unused = range(eval.size)
        indices = []
        i = 0
        sum = np.sum(eval)

        while i < count:
            i = i+1
            rand = np.random.uniform(0, sum)
            index = 0
            curr = eval[unused[index]]

            while curr < rand and index < len(unused) - 1:
                index = index + 1
                curr = curr + eval[unused[index]]

            sum = sum - eval[unused[index]]
            indices.append(unused.pop(index))

        return indices

    def create_children(self, indices):
        for i in self.__child_pop_indices:
            child = self.combine(self.population[indices[2 * i]], self.population[indices[2 * i + 1]])
            if np.random.uniform() < self.mutation_rate:
                child = self.mutate(child)

            self.__child_population[i] = child

        self.evaluate(self.__child_population, self.__child_population_eval)

        for i in self.__child_pop_indices:
            self.__next_population[self.population_size + i] = self.__child_population[i]
            self.__next_population_eval[self.population_size + i] = self.__child_population_eval[i]

    def combine(self, mom, dad):
        mask = self.reproduction_masks[random.randint(0, len(self.reproduction_masks) - 1)]
        return (mom & mask) | (dad & ~mask)

    def mutate(self, child):
        mask = self.bit_masks[random.randint(0, len(self.bit_masks) - 1)]
        return child ^ mask

    def run(self, iterations, printEvery):
        i = 0
        while i < iterations:
            i = i + 1

            for j in self.__pop_indices:
                self.__next_population[j] = self.population[j]
                self.__next_population_eval[j] = self.population_eval[j]

            self.create_children(self.select_indices(self.population_size, self.population_eval))

            indices = self.select_indices(self.population_size, self.__next_population_eval);

            for j in self.__pop_indices:
                self.population[j] = self.__next_population[indices[j]]
                self.population_eval[j] = self.__next_population_eval[indices[j]]

            if i != iterations and i % printEvery == 0:
                self.print_best();

        print("\nSOLUTION\n--------")
        self.print_best();



if __name__ == '__main__':
    test = EA(250, .1)
    test.run(250, 1)