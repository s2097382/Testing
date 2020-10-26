#Q1

def collatz(m):
    '''
    Returns the number of elements of the Collatz
    sequence starting with m.
    '''

    k = 0
    a = m
    while a != 1 :
        if a%2 == 0:
            a = a/2
        else:
            a = 3*a + 1

        k = k + 1

    return k

print(collatz(27))

#Q2

def even_sum(n):
    # Insert your code here.
    fib_1 = 1
    fib_2 = 1
    fib_new = fib_1 + fib_2

    i = 1
    sum = 0

    while fib_new <= n:
        if fib_new%2 == 0:
            sum = sum + fib_new

        fib_1 = fib_2
        fib_2 = fib_new
        fib_new = fib_1 + fib_2

    return sum

print(even_sum(3))

#Q3

def lowest_integer(f,fmin):

    nmin = 1
    while f(nmin) <= fmin:
        nmin = nmin + 1

    return nmin

def f(n):
    return n**2 + 6*n - 3

print(lowest_integer(f, 500))


#Q4

import numpy as np

def angle_dot(list1,list2):

    dot = 0
    for i in range(0,len(list1)):
        dot = dot + list1[i]*list2[i]

    angle = np.arccos(dot/(np.linalg.norm(list1)*np.linalg.norm(list2)))
    angle = round(angle*180/np.pi,1)
    dot = round(dot,1)

    return dot,angle

print(angle_dot(np.array([0., 1.]), np.array([1., 0.])))
print(angle_dot(np.array([2., -1, 1, -2]), np.array([-1., 1.5, 3., 1])))
