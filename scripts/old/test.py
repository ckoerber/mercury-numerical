from visual import*
from array import *
#from vpyton import vector 
#constant
aM=0.99 #accelersation[R0/T0**2]
vM0=0.51#velocity[R0/T0]
rM0 = 4.6 # abs[R0]
rS=0.0000003# Schwarzschildradius [R0]
dt= 2.*vM0/aM/1000 # a single time step[T0]
alpha= 0
t =0# time 
T=0#test value 
#vec_rM0=vector(0,rM0,0)#vector describing the veloctiy if t=0
#vec_vM0= vector(vM0,0,0)#vector describing the abs if t=0
vec_rM=vector(0,rM0,0)#set value for start position
vec_vM=vector(vM0,0,0)#set value for start velocity 
aMS=0
vec_aMS=vector(0,0,0)
sun= sphere(pos=(0,0,0),radius=(1),color=color.yellow)
mercury=sphere()
x0=vec_rM[0]
y0=vec_rM[1]
phi=0
#x last value of vec_rM.mag
#y indicates weather the last conditions are met by 0 = false and 1 = true 
#minimum#returns the tiniest value of vec_rM.mag

# function returning the postion and velocity of the Mercury
def calculation(vec_rM,vec_vM,alpha,rS):
 # print "test",   vec_rM,vec_vM,alpha,rS
 aMS=aM*(1+alpha*rS/vec_rM.mag)/vec_rM.mag**2
 #aMS=(aM*1+0.1/vec_rM.mag)/vec_rM.mag**2
 vec_aMS=-aMS*(vec_rM/vec_rM.mag)
 vec_rM_new=vec_rM+vec_vM*dt
 vec_vM_new=vec_vM+vec_aMS*dt
 return vec_rM_new,vec_vM_new


average_of_phi=0
all_phi=0




phiArray=array('d',[])#array of absolut values of phi
i=0#runtime expression 




while T>t : 
     
     
     vec_rM,vec_vM=calculation(vec_rM,vec_vM,alpha,rS)
     t=t+dt
     #print(vec_rM.mag)
     #mercury=sphere(pos=(vec_rM[0],vec_rM[1],vec_rM[2]),radius=((1/285.12295*10)),color=color.red)
     #rate (10000)
#      if(t==dt):                                                       
#         x=vec_rM.mag
#         
#         y=0
#      else:
#         if(x-vec_rM.mag<0 and y==1):
#             
#             minimum=x
#             phi=90-math.atan(yk/xk)*(180/math.pi)
#             phiArray.append(phi)
#             print str(phi).replace(".",",")
#         if(x-vec_rM.mag>0):
#             y=1
#         else :
#             y=0
# 
#         x=vec_rM.mag
#         xk=vec_rM[0]
#         yk=vec_rM[1]
      


print vec_rM



# while i<5:
#     phi_dif=phiArray[i+1]-phiArray[i]
#     all_phi=all_phi+phi_dif
# 
#     i =i+1
#     #print all_phi 
# 
# 
# 
# 
# average_of_phi=all_phi/5
# print average_of_phi