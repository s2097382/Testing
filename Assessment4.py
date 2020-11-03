
#Q1
import math

def primes_after(n):
    if n ==1:
        n = 2
    num = n
    while True:
        is_prime = False
        while is_prime == False:
            is_prime = True
            for i in range(2,int(math.sqrt(num))+1):
                if num%i == 0:
                    is_prime = False
            if is_prime == False:
                num = num + 1

        yield num
        num = num + 1

primes_gen = primes_after(1)
print(next(primes_gen))
primes_gen = primes_after(300)
print(next(primes_gen))
print(next(primes_gen))
from itertools import islice
print(list(islice(primes_after(n=200), 10)))


#Q2
def float_swap(x):
    if type(x)==int:
        x = float(x)
    xstr = str(x)
    my_list = xstr.split(".")
    new_str = my_list[1]+'.'+my_list[0]
    return new_str

print(float_swap(45.1234))
print(float_swap(0.1))
print(float_swap(37))

#Q3

import numpy as np
import math
def matrix_op(X,n,m):
    A = np.array([[2*(i+X)+3*(j-X) for j in range(n)] for i in range(n)])
    B = np.array([[i-math.sqrt(j+X) for j in range(n)] for i in range(n)])
    B_pow = np.linalg.matrix_power(B,m)
    prod = np.matmul(B_pow, A)
    return np.round(prod,2)

print(matrix_op(6,2,3))
print(matrix_op(2,3,2))

#Q5

def dict_build(keys,values):
    len_k = len(keys)
    len_v = len(values)

    if len_k != len_v:
        return None
    else:
        my_dict = {}
        for i in range(len_k):
            my_dict[keys[i]] = values[i]
        return my_dict

dict_build(['a','b','c'],[1,2,3])

print(dict_build(['a','b','c'],[1,2,3])== { 'a': 1,'b': 2,'c': 3 })
print(dict_build(['a','c'],[1,2,3])== None)
