<<<<<<< HEAD
# Predefined functions to use in HW

def euler(y, t, dt, derivative):
    """
    The euler method of finding the next step in solving an ODE given as y. t is time, dt is step size and derivative is a function that returns the derivative of y. 
    """
    
    y_next = y + derivative(y, t) * dt
    return y_next

def rk4(y, t, dt, derivative):
    """
    4th order runge-kutta method of solving ODEs, basically calculates the derivative of y at 4 different points in an interval and averages them. t is time, dt is step size and derivative is a function that returns the derivative of y. 
    """
    
    k1 = dt * derivative(y, t)
    k2 = dt * derivative(y + 0.5*k1, t + 0.5*dt)
    k3 = dt * derivative(y + 0.5*k2, t + 0.5*dt)
    k4 = dt * derivative(y + k3, t + dt)
    
    y_next = y + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
=======
# Predefined functions to use in HW

def euler(y, t, dt, derivative):
    """
    The euler method of finding the next step in solving an ODE given as y. t is time, dt is step size and derivative is a function that returns the derivative of y. 
    """
    
    y_next = y + derivative(y, t) * dt
    return y_next

def rk4(y, t, dt, derivative):
    """
    4th order runge-kutta method of solving ODEs, basically calculates the derivative of y at 4 different points in an interval and averages them. t is time, dt is step size and derivative is a function that returns the derivative of y. 
    """
    
    k1 = dt * derivative(y, t)
    k2 = dt * derivative(y + 0.5*k1, t + 0.5*dt)
    k3 = dt * derivative(y + 0.5*k2, t + 0.5*dt)
    k4 = dt * derivative(y + k3, t + dt)
    
    y_next = y + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
>>>>>>> origin/master
    return y_next