import random
import copy
from collections import deque

class BoneMarrow:

    def __init__(self, repair_func):
        self.libraries = []
        self.mutators = []
        self.repair_func = repair_func

    def add_complete_gene_library(self, library):
        self.libraries.append(library)

    def add_gene_library(self, gene_generator, size):
        library = []
        for i in range(size):
            library.append(gene_generator())
        self.add_complete_gene_library(library)

    def create_chromosome(self):
        if len(self.libraries) != 0:
            chromosome = copy.deepcopy(self.libraries[0][random.randint(0, len(self.libraries[0]) -1)])
            if len(self.libraries) == 1:
                return chromosome
            for i in range(1, len(self.libraries)):
                chromosome.extend(copy.deepcopy(self.libraries[i][random.randint(0, len(self.libraries[i]) -1)]))
            return self.repair_func(chromosome)

    def create_chromosomes(self, count):
        chromosomes = []
        for i in range(count):
            chromosomes.append(self.create_chromosome())
        return chromosomes

if __name__ == '__main__':
    def random_generator():
        unused = range(1, 33)
        gene = []
        for i in range(4):
            index = random.randint(0, len(unused) - 1)
            gene.append(unused.pop(index))
        return gene

    def guided_generator():
        #Optimal path seen in Figure 6.24
        path = [1, 6, 9, 15, 18, 16, 10, 2, 7, 3, 11, 19, 23, 26, 30, 32, 29, 22, 25, 28, 24, 31, 27, 20, 21, 17, 14, 8, 13, 12, 4, 5 ]
        index = random.randint(0, len(path) - 1 - 4)
        gene = []
        for i in range(4):
            gene.append(path[index + i])
        return gene

    def tsp_repair(chromosome):
        full_set = deque(range(1, 33))
        used = []
        for i in chromosome:
            if i in full_set:
                full_set.remove(i)
        for i in range(len(chromosome)):
            if chromosome[i] in used:
                chromosome[i] = full_set.popleft()
            used.append(chromosome[i])
        return chromosome

    rand_bm = BoneMarrow(tsp_repair)
    guided_bm = BoneMarrow(tsp_repair)

    for i in range(8):
        rand_bm.add_gene_library(random_generator, 4)
        guided_bm.add_gene_library(guided_generator, 4)

    print rand_bm.create_chromosomes(32)
    print guided_bm.create_chromosomes(32)