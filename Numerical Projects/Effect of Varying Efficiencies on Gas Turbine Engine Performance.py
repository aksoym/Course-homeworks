# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 17:30:04 2018

@author: Strider
"""
import matplotlib.pyplot as plt
import math

# Known parameter values.
P_1 = 101.325 #kPa
T_1 = 300 #K
T_3 = 1200 #K
k = 1.4 #ratio of specific heats

B = 79 #mm
S = 81.5 #mm
v_max = (S*math.pi*(B/2)**2)/1000 #m^3

r = 2*S
a = S/2
R = r/a
r_c = 8 #vmax/vmin

n_c = [0.6, 0.7, 0.8, 0.9, 1]
n_e = [0.6, 0.7, 0.8, 0.9, 1]


#relation between pressure and volume = p1/p2 = (vmin/vmax)^k
P_2 = (P_1)*((8)**k)

#relation between P2, T2, P3 and P4
#T_2 = 1 + ((P_2/P_1)**((k-1)/k)-1)/n_c
#P_3 = ((T_3/T_2)**(k/(k-1)))*P_2
#P_4 = (P_3)*((1/8)**k)

v_values = [v_max, v_max/8, v_max/8, v_max, v_max]
P_values = [[P_1, P_2, ], 
            [P_1, P_2, ],
            [P_1, P_2, ],
            [P_1, P_2, ],
            [P_1, P_2, ]]

print(v_values)
#iterating the P3 and P4 for varying n_c values.

for i in range(len(n_c)):
    T_2 = (1 + ((P_2/P_1)**((k-1)/k)-1)/n_c[i])*T_1
    P_3 = ((T_3/T_2)**(k/(k-1)))*P_2
    P_4 = (P_3)*((1/8)**k)
    
    print(P_3)
    
    P_values[i].append(P_3)
    P_values[i].append(P_4)
    P_values[i].append(P_1)

print (P_values)

plt.plot(v_values, P_values[0], label = 'nc = 0.6')
plt.plot(v_values, P_values[1], label = 'nc = 0.7')
plt.plot(v_values, P_values[2], label = 'nc = 0.8')
plt.plot(v_values, P_values[3], label = 'nc = 0.9')
plt.plot(v_values, P_values[4], label = 'nc = 1')
plt.ylim(0, 13000)
plt.xlim(30, 410)
plt.xlabel('Volume (m^3)')
plt.ylabel('Pressure (kPa)')
plt.legend()
plt.show()


    

    
    
