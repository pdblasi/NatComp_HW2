from __future__ import print_function
from collections import deque
import numpy as np
import math
import copy
import random

class EA:
    functions = [ '+', '*' ]
    terminals = [ '0', '1', '2', '3', '4', '5', 'x' ]

    function_positions = [0, 1, 2, 5, 8, 9, 12 ]
    terminal_positions = [3, 4, 6, 7, 10, 11, 13, 14]

    x_vals = range(-10, 11)
    y_vals = [153, 120, 91, 66, 45, 28, 15, 6, 1, 0, 3, 10, 21, 36, 55, 78, 105, 136, 171, 210, 253]

    #In prefix, looks like + + + 0 0 + 0 0 + + 0 0 + 0 0, which evaluates to a full 4 level tree that evals to 0
    default = ['+', '+', '+', '0', '0', '+', '0', '0', '+', '+',  '0', '0', '+', '0', '0']

    def __init__(self, population_size, mutation_rate):
        self.mutation_rate = mutation_rate
        self.population_size = population_size
        self.child_population_size = self.population_size // 2
        self.__child_pop_indices = range(self.child_population_size)
        self.__pop_indices = range(self.population_size)
        self.init_population()
        self.population_eval = range(self.population_size)
        self.__next_population = range(self.population_size + self.child_population_size)
        self.__next_population_eval = range(self.population_size + self.child_population_size)
        self.__child_population = range(self.child_population_size)
        self.__child_population_eval = range(self.child_population_size)

        self.evaluate(self.population, self.population_eval);

    def init_population(self):
        self.population = []
        for i in self.__pop_indices:
            individual = copy.deepcopy(self.default)
            for j in range(random.randint(7, 14)):
                self.mutate(individual);

            self.population.append(individual)

    def print_best(self):
        index = max = 0
        for i in self.__pop_indices:
            if self.population_eval[i] > max:
                max = self.population_eval[i]
                index = i

        print(" ".join(self.population[index]), "\nEval:", self.population_eval[index])
        if max != 1.0:
            print("x || y | f(x)")
            for x,y in zip(self.x_vals, self.y_vals):
                print(x, "||", y, "|", self.prefix(deque(self.population[index]), x))

    def evaluate(self, pop, eval):
        for i in range(len(pop)):
            y = map(lambda x : self.prefix(deque(pop[i]), x), self.x_vals)
            eval[i] = sum(map(lambda y : abs(y[0] - y[1]),  zip(y, self.y_vals)))
        
        #Make the smallest values into the biggest values and vice versa
        max_val = max(eval)
        for i in range(len(eval)):
            eval[i]  = float(max_val - eval[i]) / max_val

    def prefix(self, tokens, x):
        token = tokens.popleft()
        if token == '+':
                return self.prefix(tokens, x) + self.prefix(tokens, x)
        elif token == '*':
                return self.prefix(tokens, x) * self.prefix(tokens, x)
        elif token == 'x':
                return x
        else:
                return int(token)

    def select_indices(self, count, eval):
        unused = range(len(eval))
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
        self.__child_population = []
        for i in self.__child_pop_indices:
            child = self.combine(self.population[indices[2 * i]], self.population[indices[2 * i + 1]])
            if np.random.uniform() < self.mutation_rate:
                self.mutate(child)

            self.__child_population.append(child)

        self.evaluate(self.__child_population, self.__child_population_eval)

        for i in self.__child_pop_indices:
            self.__next_population[self.population_size + i] = self.__child_population[i]
            self.__next_population_eval[self.population_size + i] = self.__child_population_eval[i]

    def combine(self, mom, dad):
        i = random.randint(3, 11)
        return mom[0:i] + dad[i:]

    def mutate(self, child):
        i = random.randint(0, 14);

        if i in self.function_positions:
            child[i] = self.functions[random.randint(0, len(self.functions) - 1)]
        else:
            child[i] = self.terminals[random.randint(0, len(self.terminals) - 1)]

    def run(self, iterations, printEvery):
        i = 0
        while i < iterations and max(self.population_eval) != 1:
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
    results = []
    for i in range(100):
        test = EA(250, .1)
        test.run(1000, 1000)
        result = test.population[test.population_eval.index(max(test.population_eval))]
        if not result in results:
            results.append("{0} Eval: {1}\n{2}".format(i, max(test.population_eval), result))

    print("Unique results for 100 runs:", len(results))
    file("results.out", 'w').write("\n".join(results))


