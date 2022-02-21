import numpy
import matplotlib.pyplot

#backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
#frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

#matplotlib.pyplot.plot(backLegSensorValues, linewidth = 4, label="Back Leg")
#matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg")

targetAngles_BackLeg = numpy.load('data/targetAngles_BackLeg.npy')
targetAngles_FrontLeg = numpy.load('data/targetAngles_FrontLeg.npy')
matplotlib.pyplot.plot(targetAngles_BackLeg, label="Back Leg")
matplotlib.pyplot.plot(targetAngles_FrontLeg, label="Front Leg")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()