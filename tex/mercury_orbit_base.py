# Import all objects from the vpython module
from vpython import *

# Definition of parameters 
rM0 = 4.6    # in units of R0
vM0 = 0.51   # in units of R0/T0
c_a = 1.01   # in units of R0/T0**2
TM  = 88.    # in units of T0 
rS  = 3.e-7  # in units of R0

# Initialize distance and velocity vectors
vec_rM0 = vector(0, rM0, 0)
vec_vM0 = vector(vM0, 0, 0)

# Definition of the time step
dt = 2 * vM0 / c_a / 10

# Define the coordinate and velocity update
def evolve_mercury(vec_rM_old, vec_vM_old, alpha):
    aMS = c_a * ( 1 + alpha * rS / vec_rM_old.mag  ) / vec_rM_old.mag**2
    vec_aMS = - aMS * ( vec_rM_old / vec_rM_old.mag )
    vec_vM_new = vec_vM_old + vec_aMS * dt
    vec_rM_new = vec_rM_old + vec_vM_new * dt
    return vec_rM_new, vec_vM_new

# Define the initial coordinates; M = mercury, S = sun
M = sphere(pos=vec_rM0,       radius=0.5,  color=color.red   )
S = sphere(pos=vector(0,0,0), radius=1.5,  color=color.yellow)
M.velocity = vec_vM0
S.velocity = vector(0,0,0)
# add a visible trajectory to mercury
M.trajectory = curve(color=color.white)

# Start the simulation
t=0
alpha = 0
while t < TM:
    rate(100)
    M.trajectory.append(pos=M.pos)
    M.pos , M.velocity = evolve_mercury(M.pos , M.velocity , alpha)
    t = t + dt