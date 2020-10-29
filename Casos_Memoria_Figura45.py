#--------------------------------------------
# FIGURA 45

# 1
L = 1.04
n = 20    #discretización de 20 intervados
dx = L / n

x = np.linspace(0, L, n+1)

K = 79.5                       # m2 /s
c = 450. 					   # J / kg C
rho = 7800.             	   # kg / m3

# Arreglo con la solución
dt = 1.
Nt = 97200
alpha = (K*dt)/(c*rho*(dx**2))
u = np.zeros((Nt, n+1))

# Condiciones de borde
u[:,0] = 20.   # Borde izquierdo
u[:,-1] = 0.   # Borde derecho


# Condicion inicial
u[0, 1:n] = 20.

temperaturas = []
tiempos = []
delta = []

for k in range(Nt-1):
	t1 = perf_counter()

	t = dt*k
	tiempos.append(t/3600)
	#print(f"k = {k}, t = {t}")
	for i in range(1, n):
		u[k+1, i] = u[k,i] + alpha*(u[k,i+1] - 2*u[k,i] + u[k,i-1])
	temperaturas.append(u[k,:])
	t2 = perf_counter()

	delta = np.abs(t1-t2)


l_im1 = x[len(x)-1]/10

plot(tiempos, temperaturas)
title("x ={}m".format(round(l_im1,3)))
grid(True)
show()

#----------------------------------

# 2 
L = 2.08
n = 20    #discretización de 20 intervados
dx = L / n

x = np.linspace(0, L, n+1)

K = 79.5                       # m2 /s
c = 450. 					   # J / kg C
rho = 7800.             	   # kg / m3
# Arreglo con la solución
dt = 1.
Nt = 97200
alpha = (K*dt)/(c*rho*(dx**2))
u = np.zeros((Nt, n+1))

# Condiciones de borde
u[:,0] = 20.   # Borde izquierdo
u[:,-1] = 0.   # Borde derecho


# Condicion inicial
u[0, 1:n] = 20.

temperaturas = []
tiempos = []
delta = []

for k in range(Nt-1):
	t1 = perf_counter()

	t = dt*k
	tiempos.append(t/3600)
	#print(f"k = {k}, t = {t}")
	for i in range(1, n):
		u[k+1, i] = u[k,i] + alpha*(u[k,i+1] - 2*u[k,i] + u[k,i-1])
	temperaturas.append(u[k,:])
	t2 = perf_counter()

	delta = np.abs(t1-t2)


l_im2 = x[len(x)-1]/10


plot(tiempos, temperaturas)
title("x ={}m".format(round(l_im2,3)))
grid(True)
show()


#------------------------------------
# 3 -> x = 0,416 m

L = 4.16
n = 20    #discretización de 20 intervados
dx = L / n

x = np.linspace(0, L, n+1)

K = 79.5                       # m2 /s
c = 450. 					   # J / kg C
rho = 7800.             	   # kg / m3
# Arreglo con la solución
dt = 1.
Nt = 97200
alpha = (K*dt)/(c*rho*(dx**2))
u = np.zeros((Nt, n+1))

# Condiciones de borde
u[:,0] = 20.   # Borde izquierdo
u[:,-1] = 0.   # Borde derecho


# Condicion inicial
u[0, 1:n] = 20.

temperaturas = []
tiempos = []
delta = []

for k in range(Nt-1):
	t1 = perf_counter()

	t = dt*k
	tiempos.append(t/3600)
	#print(f"k = {k}, t = {t}")
	for i in range(1, n):
		u[k+1, i] = u[k,i] + alpha*(u[k,i+1] - 2*u[k,i] + u[k,i-1])
	temperaturas.append(u[k,:])
	t2 = perf_counter()

	delta = np.abs(t1-t2)


l_im2 = x[len(x)-1]/10

plot(tiempos, temperaturas)
title("x ={}m".format(round(l_im2,3)))
grid(True)
show()
