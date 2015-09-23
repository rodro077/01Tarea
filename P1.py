import numpy as np
import matplotlib.pyplot as plt
from pylab import *
#Se escribio un codigo para graficar el espectro del sol pedido en la pregunta 1.
datos = np.loadtxt('sun_AM0.dat')
cantidad_datos = len(datos)
x = np.zeros(cantidad_datos)
y = np.zeros(cantidad_datos)
for i in range(0,len(datos)):
	x[i] = datos[i][0]*10
	y[i] = datos[i][1]*(10^4)

plot(np.log(x),y)
xlabel('log(Longitud de Onda(Angstrom))')
ylabel('Flujo (g*cm^5*s^-3)')
title('Espectro del Sol')
grid(True)
savefig("test.png")
show()


