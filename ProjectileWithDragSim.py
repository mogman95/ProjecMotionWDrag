# Projectile motion with drag

import numpy as np
import math
import matplotlib.pyplot as plt
def nf(a):
    return np.float16(a)
m = nf(10)  # kg
A = 1 # Cross sectional area (m^2)
C = nf(1)  # Drag coefficient
roe = nf(1) # kg/m^3
g = nf(-9.81) # gravity in m/s^2
theta = nf(math.radians(0))  # Elevation of launch (deg)
v = nf(0) # Initial velocity (m/s)
x_i, y_i = nf(0), nf(0) # Initial height (m)
t_f = nf(2) # Final time (s) to then nearest 10th of a second

print(type(t_f))

t = np.array((range(np.int16(t_f*100+1))))/100

x_nd = x_i + v*np.cos(theta)*t
y_nd = y_i + v*np.sin(theta)*t + .5*g*(t**2)
x_d = np.array([])
y_d = np.array([])
vx_d = np.array([])
vy_d = np.array([])
for t_stp in t:
    x_d = np.append(x_d,[x_i + v * np.cos(theta) * t_stp])
    y_d = np.append(y_d,[y_i + v * np.sin(theta) * t_stp + .5 * g * (t_stp ** 2)])
    vy_d = np.append(vy_d, [v])
    F_D = .5*roe*C*A*(v**2)
    a = g - (F_D/m)
    v = v + a*t_stp

print(x_d)
print(x_nd)


plt.figure(figsize=(10, 10))
plt.title('Projectile Motion')
plt.xlabel('x distance (m)')
plt.ylabel('y distance (m)')
#plt.scatter(x_nd,y_nd)
plt.scatter(t,vy_d)
plt.show()
