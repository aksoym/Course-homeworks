# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 21:11:15 2018

@author: Strider
"""
import math
import numpy as np
import matplotlib.pyplot as plt


#Properties of the rod.
k = 51.9       #Thermal conductivity.
cp = 486       #Specific heat capacity.
rho = 7845     #density.
alpha = k/(cp*rho) #thermal diffusivity of the rod.


L = 1 # thickness of the wall in meters
N = 20 # number of discrete wall segments
dx = L/(N-1) # length of each wall segment in meters

total_time = 10*3600.0 # total duration of simulation in seconds
M = 500 # number of timesteps
dt = total_time/(M-1) # duration of timestep in seconds

T_initial = 0
T_boundary = 100

# initialize volume element coordinates and time samples
x = np.linspace(0, dx*(N-1), N)
timesamps = np.linspace(0, dt*(M-1), M)


#Mesh-gridding the location and time.
X, TIME = np.meshgrid(x, timesamps, indexing='ij')

#Temperature matrix initially with all elements as 0. This will be filled.
T = np.zeros((X.shape))


for i in range(len(x)):
   T[i, 0] = T_initial

for m in range(1, len(timesamps)):
    T[0, m] = T_boundary
    T[len(x)-1, m] = T_boundary



for m in range(1,len(timesamps)):
    for i in range(1, len(x)-1):
        T[i ,m] = 0 + (100-0)*(4/math.pi)*((((math.e**(-1*(math.pi)**2/2*(L**2))*alpha*m))*math.sin(math.pi*i/2*L)) + 
         ((1/3)*(math.e**((3**2)*((-math.pi)**2/2*(L**2))*alpha*m))*math.sin(3*math.pi*i/2*L)) +
         ((1/5)*(math.e**((5**2)*((-math.pi)**2/2*(L**2))*alpha*m))*math.sin(5*math.pi*i/2*L)))
        
print (T)
#3d surface projection of the matrix T.
fig1 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')
foo = ax.plot_surface(X*100, TIME/3600, T)
ax.set_xlabel('Konum (cm)')
ax.set_ylabel('Zaman (saat)')
ax.set_zlabel('Sıcaklık (C°)')
plt.show()