# Import the class vector from vpythons module visual
from vpython import *

# set up display
scene.width      = 1680
scene.height     = 1024
scene.background = color.white
scene.center     = vector(0,-2,0)

# Definition of parameters
rM0 = 4.6    # in units of R0
vM0 = 0.51   # in units of R0/T0
aM  = 1.01   # in units of R0/T0**2
TM  = 88.    # in units of T0
rS  = 3.e-7  # in units of R0

# Initialize distance and velocity vectors
vec_rM0 = vector(0, rM0, 0)
vec_vM0 = vector(vM0, 0, 0)

# define the initial coordinates; M = mercury, S = sun
M = sphere(pos=vec_rM0,       radius=0.5,  color=color.red   )
S = sphere(pos=vector(0,0,0), radius=1.5,  color=color.yellow)
# and the initial velocities
M.velocity = vec_vM0
S.velocity = vector(0,0,0)

# add a visible trajectory to mercury
M.trajectory = curve(color=color.black, radius=0.005)

# Definition of the time step
dt = 2. * vM0 / aM / 10

# Define the function
def evolve_mercury(vec_rM_old, vec_vM_old, alpha):
    # Compute the strength of the acceleration      
    aMS = aM * ( 1. + alpha * rS / vec_rM_old.mag  ) / vec_rM_old.mag**2
    # Multiply by the direction
    vec_aMS = - aMS * ( vec_rM_old / vec_rM_old.mag )
    # Update velocity vector
    vec_vM_new = vec_vM_old + vec_aMS * dt
    # Update position vector
    vec_rM_new = vec_rM_old + vec_vM_new * dt
    return vec_rM_new, vec_vM_new

# define function for angle extraction
def angle_between(v1, v2):
    return acos( dot(v1, v2) / (v1.mag * v2.mag) ) * 180. / pi

# Run parameters
alpha      = 1.e6
vec_r_last = vec_rM0
turns      = 0
max_turns  = 10
list_perih = list()
sum_angle  = 0.

# find perihelion for each turn an print it out
while turns < max_turns:
    vec_r_before_last = vec_r_last
    vec_r_last        = vector(M.pos)
    # set the frame rate: shows four earth days at once
    rate(100)
    # update the drawn trajectory with the current position
    M.trajectory.append(pos=M.pos)
    # update the velocity and position
    M.pos , M.velocity = evolve_mercury(M.pos , M.velocity , alpha)
    # check if at perihelion
    if vec_r_before_last.mag > vec_r_last.mag < M.pos.mag:
      turns = turns+1
      list_perih.append(vec_r_last)
      if turns > 1:
          # draw location of perihelion
          sphere(color=color.green, radius=0.2, pos=vec_r_last)
          # display intermediate results
          print("turn: n={n}, perihilion growth: delta Theta={angle}".format(
            n=turns, angle=angle_between(list_perih[-2],list_perih[-1])
          ))
          # note that list_perih[-2] acces the second last and
          #  list_perih[-1] the last element in the list
          sum_angle = sum_angle+angle_between(list_perih[-2],list_perih[-1])

# display the average
print("--------------------------------")
print("average perihilion growth: delta Theta={avg}".format(
  avg=sum_angle/(len(list_perih)-1)
  ))






