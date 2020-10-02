
#Q2-----------------------------------------------------------------------------
def sort_names():
    # Insert your code here
    first_name = input("Please enter the first name: ")
    second_name = input("Please enter the second name: ")

    my_list = [first_name,second_name]
    my_list.sort()
    print(f"The name that comes first alphabetically is:\n{my_list[0]}")

sort_names()

#Q3-----------------------------------------------------------------------------

import math

# Create a function for f(x)
def f(x):
    y = x**2 + 3*x + 3
    return y

# Create a function for g(x)
def g(x):
    y = math.sin(x) + 2*(x-2)/(x+1)
    return y

# Create a function for h(x)
def h(x):
    y = math.sinh(x+1) - math.exp(2*x)
    return y

# Create a function for the composition of two functions at a certain value
def composition(outer_function,inner_function, value):
    y = outer_function(inner_function(value))
    return y

# Insert the values you found for the compositions into the following statements:
print("The composition g(f(x)) when x = 5.0 equals "+str(round(composition(g,f, 5),6))+".")
print("The composition g(h(x)) when x = 5.0 equals "+str(round(composition(g,h, 5),6))+".")
print("The composition f(g(x)) when x = 2.1 equals "+str(round(composition(f,g, 2.1),6))+".")
value1 = composition(g,f, 2*math.pi)


#Q4-----------------------------------------------------------------------------
def last_two(my_string):
    if len(my_string) < 2:
        return "None"
    else:
        return my_string[-2:]

#Q5-----------------------------------------------------------------------------

def first_primes():
    my_list = list(range(2,1001))

    i = 0
    while i < len(my_list):
        #print(i)
        #print(my_list)
        #print(len(my_list))
        num = my_list[i]
        j = i + 1
        while j < len(my_list):
            if my_list[j]%num == 0 :
                my_list.remove(my_list[j])
            else:
                j = j + 1
        i = i + 1

    print(my_list)

find_primes()


#Q5-----------------------------------------------------------------------------

import math

# Create a function that calculates the value of the Taylor Polynomial
# and the error for an inputted N and x.
def taylor_ln(N, x):
    sum = 0
    i = 1
    while i <= N:
        sum = sum + ((-1)**(i+1))*((x-1)**i)/i
        i = i + 1
    error = round(abs(math.log(1.5)-sum),7)
    sum = round(sum,7)
    print(f"For N = {N}, the Taylor Polynomial equals {sum} with an error of {error}. ")

def taylor_polynomial():

    N_options = [2,4,6,8,10,12,14,16,18,20]
    # Create a for loop here to use the taylor_ln function on all of the above N values.
    x = 1.5
    for n in N_options:
        taylor_ln(n,x)


#Q7-----------------------------------------------------------------------------

def factor_list(n):
    my_list = []
    for i in range(2,int(n/2)+1):
        if n%i == 0:
            my_list.append(i)
    print(my_list)


factor_list(555)

#Q8-----------------------------------------------------------------------------

def leap_year():


    year = input("Please input the year: ")
    year = int(year)
    if year%4 != 0:
        print(f"The year {year} is not a leap year.")
    elif year%100 != 0:
        print(f"The year {year} is a leap year.")
    elif year%400 != 0:
        print(f"The year {year} is not a leap year.")
    else:
        print(f"The year {year} is a leap year.")

leap_year()

#Q9-----------------------------------------------------------------------------

days_between_dates(day1, month1, year1, day2, month2, year2)

    days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]


#Q10-----------------------------------------------------------------------------

def seasons():


    day = input("Please input an integer for the day: ")
    month = input("Please input an integer for the month: ")
    # Insert your code here.

    season = ''
    day = int(day)
    month = int(month)

    names_months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    month_name = names_months[month-1]

    days_in_months = [0,31,59,90,120,151,181,212,243,273,304,334,365]
    num_of_days = days_in_months[month-1]+day

    if (month == 2 and day == 29):
        season = 'Winter'
    elif num_of_days < 80:
        season = 'Winter'
    elif num_of_days < 172:
        season = 'Spring'
    elif num_of_days < 264:
        season = 'Summer'
    elif num_of_days < 355:
        season = 'Autumn'
    else:
        season = 'Winter'

    print(f"The {day} of {month_name} is in the {season}.")


seasons()
