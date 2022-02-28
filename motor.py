from cmath import pi
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName




    def Set_Values(self, robotId, desiredAngle):
        self.robotId = robotId
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=self.robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=c.maxForce)

