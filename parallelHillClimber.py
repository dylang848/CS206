import copy
from solution import SOLUTION
import constants as c
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.nndf")
        self.parents = {}
        self.nextAvailableID = 0

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1




    def Evolve(self):
        for i in range(len(self.parents)):
            self.parents[i].Start_Simulation("DIRECT")
        for i in range(len(self.parents)):
            self.parents[i].Wait_for_Simulation_To_End()

        #self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        #self.Show_Best()


    def Evolve_For_One_Generation(self):
        pass

        #self.Spawn()
        #self.Mutate()
        #self.child.Evaluate("DIRECT")
        #self.Print()
        #self.Select()

    def Print(self):
        print(" Parent's Fitness: " + str(self.parent.fitness) + " Child's Fitness: " + str(self.child.fitness))

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1

    def Mutate(self):
        self.child.Mutate()


    def Select(self):
        if(self.parent.fitness > self.child.fitness):
            self.parent = self.child

    def Show_Best(self):
        #os.system("python3 simulate.py GUI")
        pass