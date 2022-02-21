from cmath import pi
import random
import pybullet as p
import pybullet_data
import time
import numpy

import constants as c

import pyrosim.pyrosim as pyrosim

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)


amplitude_BackLeg = c.amplitude_BackLeg
frequency_BackLeg = c.frequency_BackLeg
phaseOffset_BackLeg = c.phaseOffset_BackLeg

amplitude_FrontLeg = c.amplitude_FrontLeg
frequency_FrontLeg = c.frequency_FrontLeg
phaseOffset_FrontLeg = c.phaseOffset_FrontLeg

targetAngles_BackLeg = numpy.array(numpy.linspace(0, 2*pi, 1000))
targetAngles_FrontLeg = numpy.array(numpy.linspace(0, 2*pi, 1000))




for i in range(1000):
    time.sleep(1/240)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    targetAngles_BackLeg[i] = amplitude_BackLeg * numpy.sin(frequency_BackLeg * targetAngles_BackLeg[i] + phaseOffset_BackLeg)
    targetAngles_FrontLeg[i] = amplitude_FrontLeg * numpy.sin(frequency_FrontLeg * targetAngles_FrontLeg[i] + phaseOffset_FrontLeg)


    pyrosim.Set_Motor_For_Joint(

        bodyIndex= robotId,

        jointName="Torso_BackLeg",

        controlMode=p.POSITION_CONTROL,

        targetPosition= targetAngles_BackLeg[i],

        maxForce=150)

    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robotId,

        jointName="Torso_FrontLeg",

        controlMode=p.POSITION_CONTROL,

        targetPosition= targetAngles_FrontLeg[i],

        maxForce=150)

p.disconnect()
numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
numpy.save('data/targetAngles_BackLeg.npy', targetAngles_BackLeg)
numpy.save('data/TargetAngles_FrontLeg', targetAngles_FrontLeg)