import pybullet as p
import pybullet_data
import time
import world
import robot


class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        self.solutionID = solutionID
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)


        self.robot = robot.ROBOT(self.solutionID)
        self.world = world.WORLD()


    def run(self):
        for i in range(1000):
            #print(i)
            if self.directOrGUI == "GUI":
                time.sleep(1 / 2400)
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()

        self.Get_Fitness()

    def Get_Fitness(self):
        self.robot.Get_Fitness(self.solutionID)


    def __del__(self):
        p.disconnect()


