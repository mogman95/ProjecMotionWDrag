# Projectile motion with drag
### imports
import numpy as np
import matplotlib.pyplot as plt
import operator as optr

###definitions
def nf(a):
    return np.float16(a)

def vsign(v,a,b):
    if v > 0:
        return optr.sub(a,b)
    elif v < 0:
        return optr.add(a,b)
    else:
        return optr.add(a,b)

###Constants
m = nf(10)  # kg
A = 1 # Cross sectional area (m^2)
C = nf(5)  # Drag coefficient
roe = nf(1) # kg/m^3
g = nf(-9.81) # gravity in m/s^2
theta = nf(np.radians(0))  # Elevation of launch (deg)
v = nf(10) # Initial velocity (m/s)
x = nf(0) # Initial x position (m)
y = nf(10) # Initial y position (m)
t_f = nf(2) # Final time (s) to then nearest 10th of a second

###Array initializations
t = np.array((range(np.int16(t_f*100+1))))/100
x_nd = x + v*np.cos(theta)*t
y_nd = y + v*np.sin(theta)*t + .5*g*(t**2)
vx_nd = v*np.cos(theta) + t*0 #<- so it fits the size of the time array
vy_nd = v*np.sin(theta) + g*t
v_nd = np.sqrt(vx_nd**2 + vy_nd**2)
x_d = np.array([])
y_d = np.array([])
vx_d = np.array([])
vy_d = np.array([])
v_d = np.array([])

###Precalculations
vx = v*np.cos(theta)
vy = v*np.sin(theta)

###for loop drag calculations
for t_stp in [.01]*int(t_f*100+1):
    F_Dx = .5 * roe * C * A * (vx ** 2)
    F_Dy = .5 * roe * C * A * (vy ** 2)
    ax = vsign(vx , 0 , (F_Dx / m))
    ay = vsign(vy , g , (F_Dy / m))
    vx = vx + ax * t_stp
    vy = vy + ay * t_stp
    x = x + vx*t_stp + .5*ax*(t_stp**2)
    y = y + vy*t_stp + .5*ay*(t_stp**2)
    x_d = np.append(x_d,[x])
    y_d = np.append(y_d,[y])
    vx_d = np.append(vx_d, [vx])
    vy_d = np.append(vy_d, [vy])
    v_d = np.append(v_d, [np.sqrt(vx_d**2 + vy_d**2)])
    #print(F_D, v)
    #if t_stp == t[9]:
    #    print("v=",type(v))
    #    break

v_trm = np.sqrt(-1*(2*m*g)/(C*roe*A))+t*0 # Terminal velocity (m/S)
#print(np.size(t))
#print(np.size(y_d))

###Visuals
plt.figure(figsize=(10, 10))
plt.title('Projectile Motion')
plt.xlabel('x Position (m)')
plt.ylabel('y Position (m)')
plt.scatter(x_nd,y_nd, color='blue')
plt.scatter(x_d,y_d, color='red')
#plt.scatter(t,-1*v_trm, color='black')
plt.legend(['No Drag','With Drag','Terminal Velocity'])
plt.show()