# comp phys with python question 4-1

from numpy import exp, arange, zeros, linspace
import matplotlib.pyplot as plt
from predefined import euler

dt = 0.1 # time interval
end_time = 700 # end time in seconds; it is NIGH
steps = end_time/dt # total number of steps the calculation is done for
n0 = 1e9 # initial number of particles
particles = zeros(steps) # preset list for storing values of remaining particles
lamb = 0.007 # decay constant
t = arange(0,end_time,dt) # time values

def radioactive_decay(state, time):
    '''
    The defining function for radioactive decay: dN/dt = -L*N where L(ambda) is the decay constant and is defined elsewhere
    '''
    return -lamb*state

particles[0] = n0 # this sets the initial value

# for the solution itself...
for i in range(int(steps-1)):
    particles[i+1] = euler(particles[i], t[i], dt, radioactive_decay)

particles_an = n0 * exp(-lamb * t) # analytical soln for comparison

# 1000 words
decaygraph = plt.figure(1)
plt.title("Radioactive Decay, Numerical vs Analytical")
plt.plot(t,particles,"ro", label="Numerical Method")
plt.plot(t,particles_an,"b-", label="Analytical Solution")
plt.legend(loc="upper right")
plt.show()