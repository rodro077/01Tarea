import numpy as np
'''
Se creo un codigo para resolver la integral de la funcion dada en el problema 3.
'''
cantidad_datos = 1000000
y = np.zeros(cantidad_datos)
x = np.linspace(0,pi/2,cantidad_datos)
for i in range(0,cantidad_datos):
    y[i] = atan(x[i])/((1+x[i]**2)*(exp(atan(x[i])-1)))

'''
se calcula la integral
'''
integral=0 ; T=5778

for i in range(0,cantidad_datos-1):
    x_dif = x[i+1]-x[i]
    y_min = min(y[i],y[i+1])
    y_max = max(y[i],y[i+1])
    arearectangulo = x_dif*y_min
    areatriangulo = (y_max-y_min)*x_dif/2
    integral = integral+arearectangulo+areatriangulo
print integral
resultado = ((2*pi*h)/c**2)*(((k*T)/h)**4)*integral
print resultado
