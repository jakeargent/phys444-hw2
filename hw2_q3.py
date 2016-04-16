# 3rd question on HW2

# JUSTIFICATION FOR PARAMETER CHANGE

# between 0-1 the solution isn't all that interesting, but with an increased range the euler method just blows up while amplitude of the oscillatory behaviour from rk method is constant. 0-1 range doesn't demonstrate this well, so I've chosen the max point to be 3.0 instead of 1.

from numpy import arange, array, zeros
from predefined import *
import matplotlib.pyplot as plt

def sec_order(state, time):
    """
    the ODE to solve is u'' + (15 + 8*x)*u = 0, with x as independent and u as dependent variable
    the state is assumed as state[0] = u, state[1] = u'
    """
    
    first_derivative = state[1]
    second_derivative = -(15+8*time)*state[0]
    
    return array([first_derivative, second_derivative])

# fluff and cruff
dx = 0.1
end_point = 3.1
steps = end_point / dx
x = arange(0, end_point, dx)
u1 = zeros([len(x),2])
u2 = zeros([len(x),2])
u1[0,1] = 0.3
u2[0,1] = 0.3

# solutions
for i in range(int(steps-1)):
    u1[i+1] = euler(u1[i],x[i],dx,sec_order)
    u2[i+1] = rk4(u2[i],x[i],dx,sec_order)

# convenience work
y1 = [u1[j,0] for j in range(len(x))]
y2 = [u2[j,0] for j in range(len(x))]
z1 = [u1[j,1] for j in range(len(x))]
z2 = [u2[j,1] for j in range(len(x))]

# over 9000
plt.figure(1)
plt.title("Euler vs Runge-Kutta")
plt.plot(x,y1,"r-",label="Euler position")
plt.plot(x,y2,"r^",label="Runge-Kutta position")
plt.plot(x,z1,"g--",label="Euler velocity")
plt.plot(x,z2,"gs",label="Runge-Kutta velocity")
plt.legend(loc="upper right")
plt.show()