#Q1

from numpy import sin,pi

def sin_calc():
    # Insert your code here
    c = sin(pi/3)
    print(c)

sin_calc()

#Q2
from numpy import pi

def sphere_calc():
    # Insert your code here
    r = 2.5
    v = round(4/3*pi*r**3,2)

    print(v)

#Q3\

def intersection():
    import math
    # Insert your code here.
    a = 2
    b = 5
    c = 5**0.5 - 1

    D = b**2-4*a*c
    x1 = round((-b+D**0.5)/(2*a),2)
    x2 = round((-b-D**0.5)/(2*a),2)

    y1 = round(1*x1**2 + 3*x1 + 5**0.5,2)
    y2 = round(1*x2**2 + 3*x2 + 5**0.5,2)

    print("Root 1:")
    print("("+str(x1)+","+str(y1)+")")
    print("Root 2:")
    print("("+str(x2)+","+str(y2)+")")

intersection()

#Q4
from numpy import * 

def numpy_log():
    i = 1
    while log(i) <= 10/i:
        i = i + 1
    print(i)

numpy_log()

#Q5

from numpy import *

def vector_angles():
    # Insert your code here.
    r1 = array([1,3,8])
    r2 = array([2,6,8])

    dot_prod = int(sum(r1*r2))

    norm_r1 = (r1[0]**2 + r1[1]**2 + r1[2]**2)**0.5
    norm_r2 = (r2[0]**2 + r2[1]**2 + r2[2]**2)**0.5

    cos_th = dot_prod/(norm_r1*norm_r2)
    theta_rad = arccos(cos_th)
    theta = round(180*pi*theta_rad,1)

    # Put the values you've found into the following print statements.
    print("The dot product of r1 and r2 is "+str(dot_prod)+".")
    print("The angle between the vectors is "+str(theta)+" degrees.")

vector_angles()


#Q6

def roman_numeral(integer):
    if integer < 2000:
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000

        output = ""
        if  integer // M != 0:
            output = output + "M"*(integer // M)
            integer = integer - M*(integer // M)
        if  integer // D != 0:
            output = output + "D"*(integer // D)
            integer = integer - D*(integer // D)
        if  integer // C != 0:
            output = output + "C"*(integer // C)
            integer = integer - C*(integer // C)
        if  integer // L != 0:
            output = output + "L"*(integer // L)
            integer = integer - L*(integer // L)
        if  integer // X != 0:
            output = output + "X"*(integer // X)
            integer = integer - X*(integer // X)
        if  integer // V != 0:
            output = output + "V"*(integer // V)
            integer = integer - V*(integer // V)
        if  integer // I != 0:
            output = output + "I"*(integer // I)
            integer = integer - I*(integer // I)

        print(output)

    else:
        print("Invalid integer - pick a smaller number.")

roman_numeral(1438)
