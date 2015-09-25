import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from scipy.constants import *
from math import *
'''
P1
A continuaciòn se recopilaran los datos del espectro del sol, mediante
el uso de un arreglo.
'''

datos = np.loadtxt('sun_AM0.dat')
cantidad_datos = len(datos)
x = np.zeros(cantidad_datos)
y = np.zeros(cantidad_datos)
for i in range(0,len(datos)):
	x[i] = datos[i][0]*10
	y[i] = datos[i][1]*(10**4)

'''
Se escribio un codigo para graficar el espectro del
Sol pedido en la pregunta 1.
'''

plot(np.log(x),y)
xlabel('log(Longitud de Onda(Angstrom))')
ylabel('Flujo (g*cm^5*s^-3)')
title('Espectro del Sol')
grid(True)
savefig("test.png")
show()


'''
Ahora se procede a calcular la integral pedida en la pregunta 2.
'''
integral=0
for i in range(0,len(datos)-1):
    x_dif = x[i+1]-x[i]
    y_min = min(y[i],y[i+1])
    y_max = max(y[i],y[i+1])
    arearectangulo=x_dif*y_min
    areatriangulo=(y_max-y_min)*x_dif/2
    integral=integral+arearectangulo+areatriangulo
'''
Finalmente calculo la luminosidad
'''
luminosidad = integral*4*pi*(au**2)
print "luminosidad", luminosidad

'''
Se creo un codigo para resolver la integral de la funcion dada en el problema 3.
'''
cantidad_datos1 = 1000000
y1 = np.zeros(cantidad_datos1)
x1 = np.linspace(0,pi/2,cantidad_datos1)
for i in range(0,cantidad_datos1):
    y1[i] = atan(x1[i])/((1+x1[i]**2)*(exp(atan(x1[i])-1)))

'''
se calcula la integral pedida.
'''
integral=0 ; T=5778

for i in range(0,cantidad_datos1-1):
    x_dif = x1[i+1]-x1[i]
    y_min = min(y1[i],y1[i+1])
    y_max = max(y1[i],y1[i+1])
    arearectangulo = x_dif*y_min
    areatriangulo = (y_max-y_min)*x_dif/2
    integral = integral+arearectangulo+areatriangulo
print integral
resultado = ((2*pi*h)/c**2)*(((k*T)/h)**4)*integral
print resultado

'''
pregunta 4
'''
'''
scipy.integrate.trapz()
scipy.integrate.quad
'''