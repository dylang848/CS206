from cmath import pi
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        if(self.jointName == "Torso_BackLeg"):
            self.amplitude = c.amplitude_BackLeg
            self.frequency = c.frequency_BackLeg
            self.offset = c.phaseOffset_BackLeg
        else:
            self.amplitude = c.amplitude_FrontLeg
            self.frequency = c.frequency_FrontLeg
            self.offset = c.phaseOffset_FrontLeg

        self.x = numpy.linspace(0, 2*pi, 1000)

        self.motorValues = numpy.zeros(1000)
        for i in range(1000):
            self.motorValues[i] = self.amplitude * numpy.sin(self.frequency * self.x[i] + self.offset)

    def Set_Values(self, robotId, timeStep):
        self.robotId = robotId
        self.timeStep =timeStep
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=self.robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[self.timeStep],
            maxForce=c.maxForce)

    def Save_Values(self):
        self.pathSaveMotors = 'data/motorsData.npy'
        numpy.save(self.pathSaveMotors, self.motorValues)