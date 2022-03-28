import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

class SOLUTION:
    def __init__(self, myID):
        self.myID = myID
        self.weights = numpy.random.rand(3,2)
        self.weights = self.weights * 2 -1

    def Evaluate(self, directOrGUI):
        pass


    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("start /B python3 simulate.py " + directOrGUI + " " + str(self.myID))

    def Wait_for_Simulation_To_End(self):
        self.fitnessFileName = str("fitness" + str(self.myID) + ".txt")
        while not os.path.exists(self.fitnessFileName):
            time.sleep(0.01)
        f = open(self.fitnessFileName, "r")
        self.fitness = float(f.read())
        f.close()
        os.system("del " +self.fitnessFileName)


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x - 3, y - 5, z - 5], size=[length, width, height])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName='Torso')
        pyrosim.Send_Sensor_Neuron(name=1, linkName='BackLeg')
        pyrosim.Send_Sensor_Neuron(name=2, linkName='FrontLeg')
        pyrosim.Send_Motor_Neuron(name=3, jointName='Torso_BackLeg')
        pyrosim.Send_Motor_Neuron(name=4, jointName='Torso_FrontLeg')

        for currentRow in range(c.numSensorNeurons):
            for currentColumnn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumnn+3,weight=self.weights[currentRow][currentColumnn])

        pyrosim.End()


    def Mutate(self):
        randomRow = random.randint(0,c.numSensorNeurons-1)
        randomColumn = random.randint(0,c.numMotorNeurons -1)
        self.weights[randomRow, randomColumn] = random.random() *2 -1

    def Set_ID(self, myID):
        self.myID = myID

