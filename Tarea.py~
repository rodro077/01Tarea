#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from pylab import *
datos = np.loadtxt('sun_AM0.dat')
cantidad_datos = len(datos)
x = np.zeros(cantidad_datos)
y = np.zeros(cantidad_datos)
for i in range(0,len(datos)):
	x[i] = datos[i][0]
	y[i] = datos[i][1]

plot(np.log(x),y)
xlabel('time (s)')
ylabel('voltage (mV)')
title('About as simple as it gets, folks')
grid(True)
savefig("test.png")
show()

