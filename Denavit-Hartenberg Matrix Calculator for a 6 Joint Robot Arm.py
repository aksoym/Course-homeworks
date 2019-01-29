import math 

#Inputs for joint parameters. If a non-number input is entered the code will return an error.
#No protection or recovery is coded against non-number input. Decimals are allowed.
print ("Please enter the joint variables.")
    
JT1_a = float(input ("Enter the 'a' parameter for joint 1: "))
JT1_alpha = math.radians(float(input ("Enter the 'alpha' parameter for joint 1: "))) #We first take the input. 
JT1_b = float(input ("Enter the 'b' variable for joint 1: "))                        #Convert it to a floating number. Then to radians.
JT1_theta = math.radians(float(input ("Enter the 'theta' variable for joint 1: ")))


JT2_a = float(input ("Enter the 'a' parameter for joint 2: "))
JT2_alpha = math.radians(float(input ("Enter the 'alpha' parameter for joint 2: ")))
JT2_b = float(input ("Enter the 'b' parameter for joint 2: "))
JT2_theta = math.radians(float(input ("Enter the 'theta' variable for joint 2: ")))


matrix_JT1 = [[round(math.cos(JT1_theta),2), round(-math.sin(JT1_theta)*math.cos(JT1_alpha),2), round(math.sin(JT1_theta)*math.sin(JT1_alpha),2), round(JT1_a*math.cos(JT1_theta),2)],
              [round(math.sin(JT1_theta),2), round(math.cos(JT1_theta)*math.cos(JT1_alpha),2), round(-math.cos(JT1_theta)*math.sin(JT1_alpha),2), round(JT1_a*math.sin(JT1_theta),2)],
              [0, round(math.sin(JT1_alpha),2), round(math.cos(JT1_alpha),2), JT1_b],
              [0, 0, 0, 1]]

matrix_JT2 = [[round(math.cos(JT2_theta),2), round(-math.sin(JT2_theta)*math.cos(JT2_alpha),2), round(math.sin(JT2_theta)*math.sin(JT2_alpha),2), round(JT2_a*math.cos(JT2_theta),2)],
              [round(math.sin(JT2_theta),2), round(math.cos(JT2_theta)*math.cos(JT2_alpha),2), round(-math.cos(JT2_theta)*math.sin(JT2_alpha),2), round(JT2_a*math.sin(JT2_theta),2)],
              [0, round(math.sin(JT2_alpha),2), round(math.cos(JT2_alpha),2), JT2_b],
              [0, 0, 0, 1]]


def matrixmult(m1,m2):
    new_matrix = [[m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0] + m1[0][2]*m2[2][0] + m1[0][3]*m2[3][0], m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1] + m1[0][2]*m2[2][1] + m1[0][3]*m2[3][1],
                   m1[0][0]*m2[0][2] + m1[0][1]*m2[1][2] + m1[0][2]*m2[2][2] + m1[0][3]*m2[3][2], m1[0][0]*m2[0][3] + m1[0][1]*m2[1][3] + m1[0][2]*m2[2][3] + m1[0][3]*m2[3][3]],    #These two row represents only 1 row in the matrix.

                  [m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0] + m1[1][2]*m2[2][0] + m1[1][3]*m2[3][0], m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1] + m1[1][2]*m2[2][1] + m1[1][3]*m2[3][1],
                   m1[1][0]*m2[0][2] + m1[1][1]*m2[1][2] + m1[1][2]*m2[2][2] + m1[1][3]*m2[3][2], m1[1][0]*m2[0][3] + m1[1][1]*m2[1][3] + m1[1][2]*m2[2][3] + m1[1][3]*m2[3][3]],

                  [m1[2][0]*m2[0][0] + m1[2][1]*m2[1][0] + m1[2][2]*m2[2][0] + m1[2][3]*m2[3][0], m1[2][0]*m2[0][1] + m1[2][1]*m2[1][1] + m1[2][2]*m2[2][1] + m1[2][3]*m2[3][1],
                   m1[2][0]*m2[0][2] + m1[2][1]*m2[1][2] + m1[2][2]*m2[2][2] + m1[2][3]*m2[3][2], m1[2][0]*m2[0][3] + m1[2][1]*m2[1][3] + m1[2][2]*m2[2][3] + m1[2][3]*m2[3][3]]

                  [m1[3][0]*m2[0][0] + m1[3][1]*m2[1][0] + m1[3][2]*m2[2][0] + m1[3][3]*m2[3][0], m1[3][0]*m2[0][1] + m1[3][1]*m2[1][1] + m1[3][2]*m2[2][1] + m1[3][3]*m2[3][1],
                   m1[3][0]*m2[0][2] + m1[3][1]*m2[1][2] + m1[3][2]*m2[2][2] + m1[3][3]*m2[3][2], m1[3][0]*m2[0][3] + m1[3][1]*m2[1][3] + m1[3][2]*m2[2][3] + m1[3][3]*m2[3][3]]]
    print (new_matrix)
                  
    

matrixmult(matrix_JT1, matrix_JT2)




JT3_a = float(input ("Enter the 'a' parameter for joint 3: "))
JT3_alpha = math.radians(float(input ("Enter the 'alpha' parameter for joint 3: ")))
JT3_b = float(input ("Enter the 'b' parameter for joint 3: "))
JT3_theta = math.radians(float(input ("Enter the 'theta' variable for joint 3: ")))              


JT4_a = float(input ("Enter the 'a' parameter for joint 4: "))
JT4_alpha = math.radians(float(input ("Enter the 'alpha' parameter for joint 4: ")))
JT4_b = float(input ("Enter the 'b' parameter for joint 4: "))
JT4_theta = math.radians(float(input ("Enter the 'theta' variable for joint 4: ")))              


JT5_a = float(input ("Enter the 'a' parameter for joint 5: "))
JT5_alpha = math.radians(float(input ("Enter the 'alpha' parameter for joint 5: ")))
JT5_b = float(input ("Enter the 'b' parameter for joint 5: "))
JT5_theta = math.radians(float(input ("Enter the 'theta' variable for joint 5: ")))              


JT6_a = float(input ("Enter the 'a' parameter for joint 6: "))
JT6_alpha = math.radians(float(input ("Enter the 'alpha' parameter for joint 6: ")))  
JT6_b = float(input ("Enter the 'b' parameter for joint 6: "))
JT6_theta = math.radians(float(input ("Enter the 'theta' variable for joint 6: ")))

#Homogenous matrix for the first joint.Round function rounds the values calculated by '2' digits.


matrix_JT1 = [[round(math.cos(JT1_theta),2), round(-math.sin(JT1_theta)*math.cos(JT1_alpha),2), round(math.sin(JT1_theta)*math.sin(JT1_alpha),2), round(JT1_a*math.cos(JT1_theta),2)],
              [round(math.sin(JT1_theta),2), round(math.cos(JT1_theta)*math.cos(JT1_alpha),2), round(-math.cos(JT1_theta)*math.sin(JT1_alpha),2), round(JT1_a*math.sin(JT1_theta),2)],
              [0, round(math.sin(JT1_alpha),2), round(math.cos(JT1_alpha),2), JT1_b],
              [0, 0, 0, 1]]

matrix_JT2 = [[round(math.cos(JT2_theta),2), round(-math.sin(JT2_theta)*math.cos(JT2_alpha),2), round(math.sin(JT2_theta)*math.sin(JT2_alpha),2), round(JT2_a*math.cos(JT2_theta),2)],
              [round(math.sin(JT2_theta),2), round(math.cos(JT2_theta)*math.cos(JT2_alpha),2), round(-math.cos(JT2_theta)*math.sin(JT2_alpha),2), round(JT2_a*math.sin(JT2_theta),2)],
              [0, round(math.sin(JT2_alpha),2), round(math.cos(JT2_alpha),2), JT2_b],
              [0, 0, 0, 1]]

matrix_JT3 = [[round(math.cos(JT3_theta),2), round(-math.sin(JT3_theta)*math.cos(JT3_alpha),2), round(math.sin(JT3_theta)*math.sin(JT3_alpha),2), round(JT3_a*math.cos(JT3_theta),2)],
              [round(math.sin(JT3_theta),2), round(math.cos(JT3_theta)*math.cos(JT3_alpha),2), round(-math.cos(JT3_theta)*math.sin(JT3_alpha),2), round(JT3_a*math.sin(JT3_theta),2)],
              [0, round(math.sin(JT3_alpha),2), round(math.cos(JT3_alpha),2), JT3_b],
              [0, 0, 0, 1]]

matrix_JT4 = [[round(math.cos(JT4_theta),2), round(-math.sin(JT4_theta)*math.cos(JT4_alpha),2), round(math.sin(JT4_theta)*math.sin(JT4_alpha),2), round(JT4_a*math.cos(JT4_theta),2)],
              [round(math.sin(JT4_theta),2), round(math.cos(JT4_theta)*math.cos(JT4_alpha),2), round(-math.cos(JT4_theta)*math.sin(JT4_alpha),2), round(JT4_a*math.sin(JT4_theta),2)],
              [0, round(math.sin(JT4_alpha),2), round(math.cos(JT4_alpha),2), JT4_b],
              [0, 0, 0, 1]]

matrix_JT5 = [[round(math.cos(JT5_theta),2), round(-math.sin(JT5_theta)*math.cos(JT5_alpha),2), round(math.sin(JT5_theta)*math.sin(JT5_alpha),2), round(JT5_a*math.cos(JT5_theta),2)],
              [round(math.sin(JT5_theta),2), round(math.cos(JT5_theta)*math.cos(JT5_alpha),2), round(-math.cos(JT5_theta)*math.sin(JT5_alpha),2), round(JT5_a*math.sin(JT5_theta),2)],
              [0, round(math.sin(JT5_alpha),2), round(math.cos(JT5_alpha),2), JT5_b],
              [0, 0, 0, 1]]

matrix_JT6 = [[round(math.cos(JT6_theta),2), round(-math.sin(JT6_theta)*math.cos(JT6_alpha),2), round(math.sin(JT6_theta)*math.sin(JT6_alpha),2), round(JT6_a*math.cos(JT6_theta),2)],
              [round(math.sin(JT6_theta),2), round(math.cos(JT6_theta)*math.cos(JT6_alpha),2), round(-math.cos(JT6_theta)*math.sin(JT6_alpha),2), round(JT6_a*math.sin(JT6_theta),2)],
              [0, round(math.sin(JT6_alpha),2), round(math.cos(JT6_alpha),2), JT6_b],
              [0, 0, 0, 1]]


def matrixmult(m1,m2):
    new_matrix = [[m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0] + m1[0][2]*m2[2][0] + m1[0][3]*m2[3][0], m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1] + m1[0][2]*m2[2][1] + m1[0][3]*m2[3][1],
                   m1[0][0]*m2[0][2] + m1[0][1]*m2[1][2] + m1[0][2]*m2[2][2] + m1[0][3]*m2[3][2], m1[0][0]*m2[0][3] + m1[0][1]*m2[1][3] + m1[0][2]*m2[2][3] + m1[0][3]*m2[3][3]],    #These two row represents only 1 row in the matrix.

                  [m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0] + m1[1][2]*m2[2][0] + m1[1][3]*m2[3][0], m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1] + m1[1][2]*m2[2][1] + m1[1][3]*m2[3][1],
                   m1[1][0]*m2[0][2] + m1[1][1]*m2[1][2] + m1[1][2]*m2[2][2] + m1[1][3]*m2[3][2], m1[1][0]*m2[0][3] + m1[1][1]*m2[1][3] + m1[1][2]*m2[2][3] + m1[1][3]*m2[3][3]],

                  [m1[2][0]*m2[0][0] + m1[2][1]*m2[1][0] + m1[2][2]*m2[2][0] + m1[2][3]*m2[3][0], m1[2][0]*m2[0][1] + m1[2][1]*m2[1][1] + m1[2][2]*m2[2][1] + m1[2][3]*m2[3][1],
                   m1[2][0]*m2[0][2] + m1[2][1]*m2[1][2] + m1[2][2]*m2[2][2] + m1[2][3]*m2[3][2], m1[2][0]*m2[0][3] + m1[2][1]*m2[1][3] + m1[2][2]*m2[2][3] + m1[2][3]*m2[3][3]]

                  [m1[3][0]*m2[0][0] + m1[3][1]*m2[1][0] + m1[3][2]*m2[2][0] + m1[3][3]*m2[3][0], m1[3][0]*m2[0][1] + m1[3][1]*m2[1][1] + m1[3][2]*m2[2][1] + m1[3][3]*m2[3][1],
                   m1[3][0]*m2[0][2] + m1[3][1]*m2[1][2] + m1[3][2]*m2[2][2] + m1[3][3]*m2[3][2], m1[3][0]*m2[0][3] + m1[3][1]*m2[1][3] + m1[3][2]*m2[2][3] + m1[3][3]*m2[3][3]]]
    print (new_matrix)
                  
    



               
 
              
