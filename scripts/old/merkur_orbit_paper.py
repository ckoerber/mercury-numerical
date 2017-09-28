#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  import the essential classes from vpythons module visual
from visual import vector, sphere, color, curve, rate, display
import numpy as np
from copy import deepcopy

# Definition of parameters
rM0 = np.float128(46)/10   # in units of R0
vM0 =  np.float128(51)/100  # in units of R0/T0
aM  =  np.float128(99)/100  # in units of R0/T0**2
T   =  np.float128(88)   # in units of T0
rS  =  3.e-7 # in units of R0

# Definition of the time step
dt =  np.float128(2) * vM0 / aM / 1000

# Define the update function
def evolve_mercury(vec_rM_old , vec_vM_old , alpha ):
	# get the magnitude of the acceleration
	aMS        = aM * ( 1 + alpha * rS / vec_rM_old.mag ) / vec_rM_old.mag**2
	# get the vector of the acceleration
	vec_aMS    = - aMS * ( vec_rM_old / vec_rM_old.mag )
	# get the new position vector of mercury
	vec_rM_new = vec_rM_old + vec_vM_old * dt
	# get the new velocity vector of mercury
	vec_vM_new = vec_vM_old + vec_aMS    * dt
	# return the new vectors
	return vec_rM_new , vec_vM_new

# Initialize distance and velocity vectors
vec_rM0 = vector(0, rM0, 0) 
vec_vM0 = vector(vM0, 0, 0)

# display the objects from now on
view = display(
	background=color.white,
	width=800,
	height=1000,
)
view.center     = (0,0,0)
view.userzoom = True
view.userspin = True

# define the initial coordinates; M= mercury, S = sun
M = sphere(pos=vec_rM0,       radius=0.1, color=color.red   ) 
S = sphere(pos=vector(0,0,0), radius=1.0,  color=color.yellow)
# and the initial velocities
M.velocity  = vec_vM0
S.velocity  = vector(0 ,0 ,0)

# add a visible trajectory to mercury
M.trajectory = curve(color=color.black)

t     = 0
alpha = 10**6

trajectory = []

# update the objects
while t < T*2:
	# set the frame rate: shows four earth days at once
	trajectory += [M.pos.mag]
	rate(40*1000)
	# update the drawn trajectory with the current position
	M.trajectory.append(pos=M.pos)
	# update the velocity and position
	M.pos , M.velocity = evolve_mercury(M.pos , M.velocity , alpha)
	# update tim
	t = t + dt

print M.pos
print np.max(trajectory)
