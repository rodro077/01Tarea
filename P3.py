from astropy.constants import *
from math import *
import numpy as np
'''
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

'''
integral=0 ; h=h.value ; c=c.value ;k=c
f_plack = ((2*pi*h))


for i in range(0,len(datos)-1):
    x_dif = x[i+1]-x[i]
    y_min = min(y[i],y[i+1])
    y_max = max(y[i],y[i+1])
    arearectangulo=x_dif*y_min
    areatriangulo=(y_max-y_min)*x_dif/2
    integral=integral+arearectangulo+areatriangulo
