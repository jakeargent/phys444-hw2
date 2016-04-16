<<<<<<< HEAD
# Solutions for Comp Phys with Python questions 4-0 and 4-2

from numpy import array, linspace, zeros, sin, sqrt
from predefined import *
import matplotlib.pyplot as plt

def general_force(state,time):
    """
    derivative function for mx'' = f(x,t) where ' denotes derivative wrt t
    state is assumed as state[0] = x, state[1] = x'
    m and the function are assumed to be defined elsewhere
    """
    
    first_derivative = state[1]
    second_derivative = function(state[0],time) / m
    
    return array([first_derivative, second_derivative])

def function(x,t):
    return -9.8

# Relevant parameters for general force
m = 1 # mass in kg
steps = 1000
tau = 10 # total time
dt = tau / (steps-1)
t = linspace(0,tau,steps)
y1 = zeros([steps,2])
y1[0,0] = 500 # initial position
y1[0,1] = 98 # initial velocity

# Why not solve eh?
for k in range(steps-1):
    y1[k+1] = euler(y1[k], t[k], dt, general_force)

# for the sake of convenience
x1 = [y1[j,0] for j in range(steps)]
v1 = [y1[j,1] for j in range(steps)]

# 1000 words for general force
general_force_graph = plt.figure(1)
plt.title("General Force ODE Solution")
plt.plot(t,x1,label="Coordinate")
plt.plot(t,v1,label="Change in Coordinate")
plt.legend(loc="upper right")

def gen_sec_order(state,time):
    """
    general equation for second order non-homogeneous differential equation
    Ax'' + Bx' + Cx = D
    the constants are assumed to be defined elsewhere
    state is assumed as state[0] = x, state[1] = x'
    """
    
    first_derivative = state[1]
    second_derivative = (D - C*state[0] - B*first_derivative) / A
    
    return array([first_derivative, second_derivative])

# Relevant parameters for general second order ODE
# If a parameter is unspecified below for gen_sec_order but supplied to the function then the variable defined somewhere above has been used since the actual boundary conditions don't matter and the solutions are only here to check whether the definition of ODEs works or not
A = 3
B = 4
C = 5
D = 10
y2 = zeros([steps,2])
y2[0,0] = 120 # initial coordinate
y2[0,1] = 5 # initial change in coordinate

# Solution
for k in range(steps-1):
    y2[k+1] = euler(y2[k], t[k], dt, gen_sec_order)

# convenience
x2 = [y2[j,0] for j in range(steps)]
v2 = [y2[j,1] for j in range(steps)]

# visualization
gen_sec_order_graph = plt.figure(2)
plt.title("General Second Order ODE Solution")
plt.plot(t,x2,label="Position")
plt.plot(t,v2,label="Velocity")
plt.legend(loc="upper right")

def oscillatory(state,time):
    """
    A seemingly oscillatory ODE that's quite nonlinear, it's equation is
    mx'' = -sqrt(g/L)sin(T) - B*x' + h * sin(w*t)
    m, g, L, B, h and w are assumed to be defined elsewhere
    state is assumed as state[0] = x, state[1] = x'
    """
    
    first_derivative = state[1]
    second_derivative = (-sqrt(g/L)*sin(state[0]) -B*first_derivative + h*sin(w*time)) / m
    
    return array([first_derivative, second_derivative])

# Relevant parameters for oscillatory ODE
# If a parameter is unspecified below for oscillatory but supplied to the function then the variable defined somewhere above has been used since the actual boundary conditions don't matter and the solutions are only here to check whether the definition of ODEs works or not
g = 9.8
L = 2
h = 200
w = 5
y3 = zeros([steps,2])
y3[0,0] = 0 # initial coordinate
y3[0,1] = 0 # initial change in coordinate

# Solution
for k in range(steps-1):
    y3[k+1] = euler(y3[k], t[k], dt, oscillatory)

# convenience
x3 = [y3[j,0] for j in range(steps)]
v3 = [y3[j,1] for j in range(steps)]

# visualization
oscillatory_graph = plt.figure(3)
plt.title("Oscillatory ODE Solution")
plt.plot(t,x3,label="Angle")
plt.plot(t,v3,label="Angular Velocity")
plt.legend(loc="upper right")

def unitary_third_order(state, time):
    """
    3rd order ODE with all constants 1, its equation is
    x''' + x'' + x' + x = 0
    state is assumed to be state[0] = x, state[1] = x' and state[2] = x'' 
    """
    
    first_derivative = state[1]
    second_derivative = state[2]
    third_derivative = -second_derivative - first_derivative - state[0]
    
    return array([first_derivative, second_derivative, third_derivative])

# Relevant parameters for 3rd order ODE
# If a parameter is unspecified below for unitary_third_order but supplied to the function then the variable defined somewhere above has been used since the actual boundary conditions don't matter and the solutions are only here to check whether the definition of ODEs works or not
y4 = zeros([steps,3])
y4[0,0] = 500 # initial coordinate
y4[0,1] = 300 # initial change in coordinate
y4[0,2] = 100 # initial change in change in coordinate

# Solution
for k in range(steps-1):
    y4[k+1] = euler(y4[k], t[k], dt, unitary_third_order)

# convenience
x4 = [y4[j,0] for j in range(steps)]
v4 = [y4[j,1] for j in range(steps)]
z4 = [y4[j,2] for j in range(steps)]

# visualization
unitary_third_order_graph = plt.figure(4)
plt.title("Unitary Third Order ODE Solution")
plt.plot(t,x4,label="Position")
plt.plot(t,v4,label="Velocity")
plt.plot(t,z4,label="Acceleration")
plt.legend(loc="upper right")
=======
# Solutions for Comp Phys with Python questions 4-0 and 4-2

from numpy import array, linspace, zeros, sin, sqrt
from predefined import *
import matplotlib.pyplot as plt

def general_force(state,time):
    """
    derivative function for mx'' = f(x,t) where ' denotes derivative wrt t
    state is assumed as state[0] = x, state[1] = x'
    m and the function are assumed to be defined elsewhere
    """
    
    first_derivative = state[1]
    second_derivative = function(state[0],time) / m
    
    return array([first_derivative, second_derivative])

def function(x,t):
    return -9.8

# Relevant parameters for general force
m = 1 # mass in kg
steps = 1000
tau = 10 # total time
dt = tau / (steps-1)
t = linspace(0,tau,steps)
y1 = zeros([steps,2])
y1[0,0] = 500 # initial position
y1[0,1] = 98 # initial velocity

# Why not solve eh?
for k in range(steps-1):
    y1[k+1] = euler(y1[k], t[k], dt, general_force)

# for the sake of convenience
x1 = [y1[j,0] for j in range(steps)]
v1 = [y1[j,1] for j in range(steps)]

# 1000 words for general force
general_force_graph = plt.figure(1)
plt.title("General Force ODE Solution")
plt.plot(t,x1,label="Coordinate")
plt.plot(t,v1,label="Change in Coordinate")
plt.legend(loc="upper right")

def gen_sec_order(state,time):
    """
    general equation for second order non-homogeneous differential equation
    Ax'' + Bx' + Cx = D
    the constants are assumed to be defined elsewhere
    state is assumed as state[0] = x, state[1] = x'
    """
    
    first_derivative = state[1]
    second_derivative = (D - C*state[0] - B*first_derivative) / A
    
    return array([first_derivative, second_derivative])

# Relevant parameters for general second order ODE
# If a parameter is unspecified below for gen_sec_order but supplied to the function then the variable defined somewhere above has been used since the actual boundary conditions don't matter and the solutions are only here to check whether the definition of ODEs works or not
A = 3
B = 4
C = 5
D = 10
y2 = zeros([steps,2])
y2[0,0] = 120 # initial coordinate
y2[0,1] = 5 # initial change in coordinate

# Solution
for k in range(steps-1):
    y2[k+1] = euler(y2[k], t[k], dt, gen_sec_order)

# convenience
x2 = [y2[j,0] for j in range(steps)]
v2 = [y2[j,1] for j in range(steps)]

# visualization
gen_sec_order_graph = plt.figure(2)
plt.title("General Second Order ODE Solution")
plt.plot(t,x2,label="Position")
plt.plot(t,v2,label="Velocity")
plt.legend(loc="upper right")

def oscillatory(state,time):
    """
    A seemingly oscillatory ODE that's quite nonlinear, it's equation is
    mx'' = -sqrt(g/L)sin(T) - B*x' + h * sin(w*t)
    m, g, L, B, h and w are assumed to be defined elsewhere
    state is assumed as state[0] = x, state[1] = x'
    """
    
    first_derivative = state[1]
    second_derivative = (-sqrt(g/L)*sin(state[0]) -B*first_derivative + h*sin(w*time)) / m
    
    return array([first_derivative, second_derivative])

# Relevant parameters for oscillatory ODE
# If a parameter is unspecified below for oscillatory but supplied to the function then the variable defined somewhere above has been used since the actual boundary conditions don't matter and the solutions are only here to check whether the definition of ODEs works or not
g = 9.8
L = 2
h = 200
w = 5
y3 = zeros([steps,2])
y3[0,0] = 0 # initial coordinate
y3[0,1] = 0 # initial change in coordinate

# Solution
for k in range(steps-1):
    y3[k+1] = euler(y3[k], t[k], dt, oscillatory)

# convenience
x3 = [y3[j,0] for j in range(steps)]
v3 = [y3[j,1] for j in range(steps)]

# visualization
oscillatory_graph = plt.figure(3)
plt.title("Oscillatory ODE Solution")
plt.plot(t,x3,label="Angle")
plt.plot(t,v3,label="Angular Velocity")
plt.legend(loc="upper right")

def unitary_third_order(state, time):
    """
    3rd order ODE with all constants 1, its equation is
    x''' + x'' + x' + x = 0
    state is assumed to be state[0] = x, state[1] = x' and state[2] = x'' 
    """
    
    first_derivative = state[1]
    second_derivative = state[2]
    third_derivative = -second_derivative - first_derivative - state[0]
    
    return array([first_derivative, second_derivative, third_derivative])

# Relevant parameters for 3rd order ODE
# If a parameter is unspecified below for unitary_third_order but supplied to the function then the variable defined somewhere above has been used since the actual boundary conditions don't matter and the solutions are only here to check whether the definition of ODEs works or not
y4 = zeros([steps,3])
y4[0,0] = 500 # initial coordinate
y4[0,1] = 300 # initial change in coordinate
y4[0,2] = 100 # initial change in change in coordinate

# Solution
for k in range(steps-1):
    y4[k+1] = euler(y4[k], t[k], dt, unitary_third_order)

# convenience
x4 = [y4[j,0] for j in range(steps)]
v4 = [y4[j,1] for j in range(steps)]
z4 = [y4[j,2] for j in range(steps)]

# visualization
unitary_third_order_graph = plt.figure(4)
plt.title("Unitary Third Order ODE Solution")
plt.plot(t,x4,label="Position")
plt.plot(t,v4,label="Velocity")
plt.plot(t,z4,label="Acceleration")
plt.legend(loc="upper right")
>>>>>>> origin/master
plt.show()