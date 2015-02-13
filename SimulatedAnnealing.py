from __future__ import print_function
import numpy as np
import math

class SimulatedAnnealing:

    def __init__(self, eval, perturb, x, T, tempChange, stop):
        self.eval = eval
        self.perturb = perturb
        self.x = x
        self.T = T
        self.tempChange = tempChange
        self.stop = stop

    def Anneal(self):
        t = 0
        e = self.eval(self.x)

        while not self.stop(self.T, t, self.x):
            t = t + 1
            x = self.perturb(self.x)

            e_new = self.eval(x)

            if t % 10 == 0:
                print('Iteration ', t, ': x = ', self.x, ' | Energy = ', e, sep='')

            if e_new > e or np.random.uniform(0, 1) < math.exp((e_new - e) / self.T):
                self.x = x
                e = e_new

            self.T = self.tempChange(self.T, t)
            
        print('Iteration ', t, ': x = ', self.x, ' | Energy = ', e, sep='')

if __name__ == "__main__":
    def eval(x):
        return (2 ** (-2 * (((x - 0.1)/.9) * ((x - 0.1)/.9))) * math.sin(5 * math.pi * x) ** 6)

    def perturb(x):
        x_new = x + np.random.normal(0, .2)

        while not (x_new <= 1 and x_new >= 0):
            x_new = x + np.random.normal(0, .2)

        return x_new

    def tempChange(T, t):
        return T / 2

    def stop(T, t, x):
        return t == 100;

    simulatedAnnealing = SimulatedAnnealing(eval, perturb, np.random.uniform(0, 1), 1000.0, tempChange, stop);
    simulatedAnnealing.Anneal();