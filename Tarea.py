#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from pylab import *
datos = np.loadtxt('sun_AM0.dat')
i = arange(0, len(datos), 1)
x = datos[i-1]
y = datos[i]
plot(x[i],y[i])
print i

xlabel('time (s)')
ylabel('voltage (mV)')
title('About as simple as it gets, folks')
grid(True)
savefig("test.png")
show()

