from sympy import *
import matplotlib.pyplot as plt
import numpy as np

#Defining the symbols and the formula.
M,a = symbols('M a')

ramF = (M*(1.4*287*288)**(1/2))*((((1+0.02)*(a)**(1/2))/(1+((1.4-1)/2)*(M**2))**0.5)-1)

#Using sympy to get the derivative.

ramjetPrime = ramF.diff(M)

#These are the lists to plot the graphic. These will be filled as the calculations are made.

Mvalues = []
aValues = []
AnalyticalValues = []
CalculatedAlpha = [5,6,7,8,9,10,11,12] #These are the values to be used in analytical formula.

#Numerical calculations are made with alpha varying from 5 to 12 in 14 points.

for i in np.linspace(5,12,14):
    y = ramjetPrime.subs(a,i)
    real_solution = solve(y, M) #solve function solves the equation for M.
    positive_solution = list(filter(lambda x: x >0, real_solution)) #filtering positive results.
    Mvalues.append(positive_solution) #Adding the calculated values to the list for plotting.
    aValues.append(i)


#Analytically derived formula of optimal M, in terms of α.
#Solving for values from 5 to 12.

for x in range(5,13):
    y = ((((1.02*x**(0.5))**(2/3)-1)*2)/(0.4))**(0.5) 
    AnalyticalValues.append(y)

#Plotting.

plt.plot(aValues,Mvalues, 'r-')
plt.scatter(CalculatedAlpha,AnalyticalValues, s=20, color='green')
plt.title('Optimal Mach Number for Different Values of α')
plt.xlabel('α (Temp. ratio of the cycle)')
plt.ylabel('Optimal Mach Number')
plt.xlim(4.5,12.5)
plt.ylim(1,3)
plt.legend(['Numerical', 'Analytically Calculated'], loc='lower right')


plt.show()





    









