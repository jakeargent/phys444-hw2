<<<<<<< HEAD
# Second question on HW2

# PLEASE READ THIS - JUSTIFICATION FOR CHANGING SOME PARAMETERS

# Runge-Kutta is supposed to be a better method than euler, so it doesn't make much sense to compare them with RK having lesser step size, hence I've interchanged them, although it would be better if we had an analytical solution to compare

# When solved in range 0-1, solutions change direction and take a nosedive in an absurd manner, but when the range is increased this is gone. 0-1 range thus, may be misleading so I've changed that too. (at end_point = 1.1, 1.2, 1.4 there is some really weird behaviour.)

# Apparently the solution to this DE blows up towards negative infinity at some point after x=6, because the negative quadratic term dominates heavily against sin(x) as x increases

from numpy import arange, array, power, sin, zeros
from predefined import *
import matplotlib.pyplot as plt

def squared_sined(state, time):
    """
    derivative function for u' = -u**2 + sin(x), with x as the independent variable and u the dependent
    """
    
    derivative = -power(state,2) + sin(time)
    return derivative

# Solution with euler's method
euler_dx = 0.1 # step size
euler_end_point = 1.6
euler_steps = euler_end_point / euler_dx # number of steps of calculation
euler_x = arange(0,euler_end_point, euler_dx) # range of independent variable
euler_u = zeros(len(euler_x))

for i in range(int(euler_steps-1)):
    euler_u[i+1] = euler(euler_u[i], euler_x[i], euler_dx, squared_sined)

# Solution with 4th order runge-kutta method
rk_dx = 0.2 # step size
rk_end_point = 1.6
rk_steps = rk_end_point / rk_dx # number of steps of calculation
rk_x = arange(0,rk_end_point, rk_dx) # range of independent variable
rk_u = zeros(len(rk_x))

for i in range(int(rk_steps-1)):
    rk_u[i+1] = euler(rk_u[i], rk_x[i], rk_dx, squared_sined)

print("From euler's method u(x=0.4) = ", euler_u[4])
print("From runge-kutta method u(x=0.4) = ", rk_u[2])

# A graph is worth some words
plt.figure(1)
plt.title("Euler vs Runge-Kutta")
plt.plot(euler_x, euler_u, "g-.", label="Euler")
plt.plot(rk_x, rk_u, "r-", label="Runge-Kutta")
plt.legend(loc="upper right")
=======
# Second question on HW2

# PLEASE READ THIS - JUSTIFICATION FOR CHANGING SOME PARAMETERS

# Runge-Kutta is supposed to be a better method than euler, so it doesn't make much sense to compare them with RK having lesser step size, hence I've interchanged them, although it would be better if we had an analytical solution to compare

# When solved in range 0-1, solutions change direction and take a nosedive in an absurd manner, but when the range is increased this is gone. 0-1 range thus, may be misleading so I've changed that too. (at end_point = 1.1, 1.2, 1.4 there is some really weird behaviour.)

# Apparently the solution to this DE blows up towards negative infinity at some point after x=6, because the negative quadratic term dominates heavily against sin(x) as x increases

from numpy import arange, array, power, sin, zeros
from predefined import *
import matplotlib.pyplot as plt

def squared_sined(state, time):
    """
    derivative function for u' = -u**2 + sin(x), with x as the independent variable and u the dependent
    """
    
    derivative = -power(state,2) + sin(time)
    return derivative

# Solution with euler's method
euler_dx = 0.1 # step size
euler_end_point = 1.6
euler_steps = euler_end_point / euler_dx # number of steps of calculation
euler_x = arange(0,euler_end_point, euler_dx) # range of independent variable
euler_u = zeros(len(euler_x))

for i in range(int(euler_steps-1)):
    euler_u[i+1] = euler(euler_u[i], euler_x[i], euler_dx, squared_sined)

# Solution with 4th order runge-kutta method
rk_dx = 0.2 # step size
rk_end_point = 1.6
rk_steps = rk_end_point / rk_dx # number of steps of calculation
rk_x = arange(0,rk_end_point, rk_dx) # range of independent variable
rk_u = zeros(len(rk_x))

for i in range(int(rk_steps-1)):
    rk_u[i+1] = euler(rk_u[i], rk_x[i], rk_dx, squared_sined)

print("From euler's method u(x=0.4) = ", euler_u[4])
print("From runge-kutta method u(x=0.4) = ", rk_u[2])

# A graph is worth some words
plt.figure(1)
plt.title("Euler vs Runge-Kutta")
plt.plot(euler_x, euler_u, "g-.", label="Euler")
plt.plot(rk_x, rk_u, "r-", label="Runge-Kutta")
plt.legend(loc="upper right")
>>>>>>> origin/master
plt.show()