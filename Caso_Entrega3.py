# Ecuacion del calor 1-D
from matplotlib.pylab import *
import numpy as np
from time import perf_counter

L = 1.04
n = 20    #discretización de 20 intervados
dx = L / n

x = np.linspace(0, L, n+1)

K = 79.5                       # m2 /s
c = 450. 					   # J / kg C
rho = 7800.             	   # kg / m3

#-------------------------------------------
# CASO PLANTEADO 

# Arreglo con la solución
dt = 2.
Nt = 50000
alpha = (K*dt)/(c*rho*(dx**2))
u = np.zeros((Nt, n+1))

# Condiciones de borde
u[:,-1] = 20.  # Borde derecho

# Condicion inicial
u[0, 0:n] = 20


#du => u[k+1,i] - u[k,i] = 5
# u[k+1, i] - 5*dx = u[k,i]

for k in range(Nt-1):
	t = dt*k
	#print(f"k = {k}, t = {t}")
	u[k,0] = -(5*dx) + u[k+1,n]
	for i in range(1, n):
		u[k+1, i] = u[k,i] + alpha*(u[k,i+1] - 2*u[k,i] + u[k,i-1])
	if k%1000==0:
		plot(x, u[k,:])

l_im1 = x[len(x)-1]/10
title("Caso E3 - Nt ={}".format(Nt))
show()