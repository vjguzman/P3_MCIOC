# Ecuacion del calor 1-D
from matplotlib.pylab import *
import numpy as np

L = 1.0
n = 100 #discretización de 100 intervados
dx = L / n

x = np.linspace(0, L, n+1)

# Arreglo con la solución
dt = 1.
Nt = 5000
u = np.zeros((Nt, n+1))

K = 79.5                       # m2 /s
c = 450. 					   # J / kg C
rho = 7800.             	   # kg / m3
alpha = (K*dt)/(c*rho*(dx**2))


# Condiciones de borde
u[:,0] = 0.   # Borde izquierdo
u[:,-1] = 10.  # Borde derecho

# Condicion inicial
u[0, 1:n] = 15

for k in range(Nt-1):
	t = dt*k
	print(f"k = {k}, t = {t}")
	for i in range(1, n):
		u[k+1, i] = u[k,i] + alpha*(u[k,i+1] - 2*u[k,i] + u[k,i-1])

	if k % 200 == 0:
		plot(x, u[k, :])

title("k = {}    t = {} s".format(k, k*dt))

show()