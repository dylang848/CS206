from cmath import pi
import random
import pybullet as p
import pybullet_data
import time
import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
import world
import robot
import sensor
import motor

class SIMULATION:
    def __init__(self):


        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        self.robotId = robot.ROBOT()

        self.world = world.WORLD()
        self.sensor = sensor.SENSOR()
        self.motor = motor.MOTOR()



    def run(self):
        for i in range(1000):
            print(i)
            time.sleep(1 / 240)
            p.stepSimulation()
            '''
            backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

            targetAngles_BackLeg[i] = amplitude_BackLeg * numpy.sin(
                frequency_BackLeg * targetAngles_BackLeg[i] + phaseOffset_BackLeg)
            targetAngles_FrontLeg[i] = amplitude_FrontLeg * numpy.sin(
                frequency_FrontLeg * targetAngles_FrontLeg[i] + phaseOffset_FrontLeg)

            pyrosim.Set_Motor_For_Joint(

                bodyIndex=robotId,

                jointName="Torso_BackLeg",

                controlMode=p.POSITION_CONTROL,

                targetPosition=targetAngles_BackLeg[i],

                maxForce=150)

            pyrosim.Set_Motor_For_Joint(

                bodyIndex=robotId,

                jointName="Torso_FrontLeg",

                controlMode=p.POSITION_CONTROL,

                targetPosition=targetAngles_FrontLeg[i],

                maxForce=150)

    '''

    def __del__(self):
        p.disconnect()

