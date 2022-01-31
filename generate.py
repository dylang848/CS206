import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

pyrosim.Start_SDF("boxes.sdf")

for x in range(0, 8):
    for y in range(0,8):
        z=0
        length = 1
        width = 1
        height = 1
        for z in range(0,8):
            pyrosim.Send_Cube(name="Box", pos=[x, y, z+.5] , size=[length, width, height])
            length = .9*length
            width = .9*width
            height = .9*height






pyrosim.End()