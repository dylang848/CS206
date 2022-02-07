import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

matplotlib.pyplot.plot(backLegSensorValues, linewidth = 4, label="Back Leg")
matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg")


matplotlib.pyplot.legend()
matplotlib.pyplot.show()