import pybullet as p
import pyrosim.pyrosim as pyrosim
import os
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c
import numpy

from sensor import SENSOR
from motor import MOTOR


class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain" + self.solutionID + ".nndf")
        #os.system("del brain" + self.solutionID + ".nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, timeStep):
        self.timeStep = timeStep
        for i in self.sensors:
            if(i == "LowerFrontLeg"):
                self.sensorI = numpy.sin(500 * timeStep)
            else:
                self.sensor = self.sensors[i]
                self.sensor.Get_Value(self.timeStep)





            #self.sensor = self.sensors[i]
            #self.sensor.Get_Value(self.timeStep)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Values(self.robotId, desiredAngle)



    def Get_Fitness(self, solutionID):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        f = open("tmp" + solutionID + ".txt", "w")
        f.write(str(xPosition))
        f.close()
        os.system("rename tmp" + str(solutionID) + ".txt fitness" + str(solutionID) + ".txt")
        exit()