import copy
from solution import SOLUTION
import constants as c
import os

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()


    def Evolve(self):
        self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        self.Show_Best()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Print(self):
        print(" Parent's Fitness: " + str(self.parent.fitness) + " Child's Fitness: " + str(self.child.fitness))

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()


    def Select(self):
        if(self.parent.fitness > self.child.fitness):
            self.parent = self.child

    def Show_Best(self):
        os.system("python3 simulate.py GUI")