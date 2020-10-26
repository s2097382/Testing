#Q1

def chess_board():
    # Insert your code here x
    user_input = input("Please input the location of the square:")
    letter = ord(user_input[0]) - 96
    number = int(user_input[1:])

    if number > 8 or letter > 8:
        print("This square is not on the board.")
    else:
        if number%2 == 0 and letter%2 == 0:
            print(f"The square {user_input} is black.")
        elif number%2 == 1 and letter%2 == 1:
            print(f"The square {user_input} is black.")
        else:
            print(f"The square {user_input} is white.")

chess_board()

#Q2

def window(windows_list):


    my_list = []
    for w in windows_list:
        if w < 50 and w > 10:
            my_list.append(w)

    return my_list

print(window([1, 2, 3, 20]))
print(window([40, 0, 30, 10, -50]))

#Q3

def move_a(my_str):

    my_list = list(my_str)
    extra = []

    count = 0
    i = 0
    while i < len(my_list):
        if my_list[i] == 'a':
            del(my_list[i])
            count = count + 1
            extra.append('a')
        else:
            i = i + 1

    for i in extra:
        my_list.append(i)

    my_str = "".join(my_list)

    return my_str


move_a('abc')

#Q4


def diff_type(x,y):

    return type(x) != type(y)

#Q5

def joini(my_list):

    my_str = ""
    for i in my_list:
        my_str = my_str + str(i)
    return my_str

print(joini([2,34,56,7]))

#Q6s

def intersection():
    import math
    # Insert your code here.

    x1 = (-5+math.sqrt(25-8*(math.sqrt(5)-1)))/4
    y1 = -x1**2-2*x1+1
    x2 = (-5-math.sqrt(25-8*(math.sqrt(5)-1)))/4
    y2 = -x2**2-2*x2+1

    print("Root 1:")
    print(f"({x1}, {y1})")
    print("Root 2:")
    print(f"({x2}, {y2})")

#Q7

def dice(n):

    from numpy import random
    vals = random.randint(1,7,size = n)
    return list(vals)


dice(20)
