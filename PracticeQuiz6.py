#Q1

def joini(input):
    output = ""
    for x in input:
        output = output + str(x)

    return int(output)


print(joini([2,34,56,7]))

#Q2

a = [[181, 91], [152, 58], [168, 75], [162, 76], [174, 85], [161, 60], [192, 101], [178, 85]]

# A function that calculates the average height of a list
def average_height(b):
    n = len(b)
    sum_h = 0
    for x in b:
        sum_h = sum_h + x[0]
    return sum_h/n

# A function that calculates the average weight of a list
def average_weight(b):
    n = len(b)
    sum_w = 0
    for x in b:
        sum_w = sum_w + x[1]
    return sum_w/n

# A function that calculates and prints values for the average heights and
# weights for the class with and without the new student.
def student_list():

    a = [[181, 91], [152, 58], [168, 75], [162, 76], [174, 85], [161, 60], [192, 101], [178, 85]]

    print(f'The original average height of the class is {average_height(a)} cm.')
    print(f'The original average weight of the class is {average_weight(a)} kg.')

    a.append([180,89])
    print(f'The new average height of the class is {average_height(a)} cm.')
    print(f'The new average weight of the class is {average_weight(a)} kg.')

    a.sort(key=lambda x: x[1])
    print(a)

student_list()

#Q3

def diff_type(x,y):

    if type(x)==type(y):
         return False
    else:
         return True

#Q4

def list_triples(amin,cmax):
    my_list = []
    for a in range(amin,cmax-1):
        for b in range(a+1,cmax):
            for c in range(b+1,cmax+1):
                if a**2 + 2*b**2 == c**2:
                    my_list.append((a,b,c))
    return my_list

U = list_triples(3,9)
U.sort()
print(U)

#Q5
