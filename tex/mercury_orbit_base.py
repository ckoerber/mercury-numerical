# Import all objects from the vpython module
from vpython import *

# Definition of physical parameters
rM0 = 4.60    # Initial radius of Mercury orbit, in units of R0
vM0 = 5.10e-1 # Initial orbital speed of Mercury, in units of R0/T0
c_a = 9.90e-1 # Base acceleration of Mercury, in units of R0**3/T0**2
TM  = 8.80e+1 # Orbit period of Mercury
rS  = 2.95e-7 # Schwarzschild radius of Sun,in units of R0
rL2 = 8.19e-7 # Specific angular momentum, in units of R0**2

# Define the initial coordinates; M = mercury, S = Sun
M = sphere(pos=vector(0, rM0, 0), radius=0.5,  color=color.red   )
S = sphere(pos=vector(0, 0, 0),   radius=1.5,  color=color.yellow)
# And the initial velocities
M.velocity = vector(vM0, 0, 0)
S.velocity = vector(0, 0, 0)

# Add a visible trajectory to mercury
M.trajectory = curve(color=color.white)

# Definition of the time step
dt = 2 * vM0 / c_a / 20

# Define the coordinate and velocity update
def evolve_mercury(vec_rM_old, vec_vM_old, alpha, beta):
    # Compute the strength of the acceleration
    temp = 1 + alpha * rS / vec_rM_old.mag + beta * rL2 / vec_rM_old.mag**2
    aMS  = c_a * temp / vec_rM_old.mag**2
    # Multiply by the direction
    vec_aMS = - aMS * ( vec_rM_old / vec_rM_old.mag )
    # Update velocity vector
    vec_vM_new = vec_vM_old + vec_aMS * dt
    # Update position vector
    vec_rM_new = vec_rM_old + vec_vM_new * dt
    return vec_rM_new, vec_vM_new

t     = 0.0
alpha = 0.0
beta  = 0.0
# Execute the loop as long as t < 2*TM
while t < 2*TM:
    # Set the frame rate (you can choose a higher rate to accelerate the program)
    rate(100)
    # Update the drawn trajectory with the current position
    M.trajectory.append(pos=M.pos)
    # Update velocity and position
    M.pos, M.velocity = evolve_mercury(M.pos , M.velocity , alpha, beta)
    # Advance time by one step
    t = t + dt
