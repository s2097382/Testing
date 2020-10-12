#Q1

def student_pass(score1, score2, score3):
    # Insert your code here
    passed = False
    avg = (score1 + score2 + score3)/3

    if score1 >= 40 and score2>= 40 and score3 >= 40:
        passed = True
    elif avg > 50:
        if score1>=40 and score2>=40:
            passed = True
        elif score1>=40 and score3>=40:
            passed = True
        elif score2>=40 and score3>=40:
            passed = True

    if passed:
        print("This student has passed.")
    else:
        print("This student has not passed.")

student_pass(90,39,39)

#Q2

# Create a function that determines whether the given year is a leap year.
def is_leap(year):
    # You should have made this function (leap_year) in a previous problem.
    year = int(year)
    if year%4 != 0:
        leap = False
    elif year%100 != 0:
        leap = True
    elif year%400 != 0:
        leap = False
    else:
        leap = True
    return(leap)

# Create a function to calculate the number of days since 1/1/1901 for a given date.
def days_since(day, month, year):

    days_in_months = [0,31,59,90,120,151,181,212,243,273,304,334,365]
    days_in_months_leap = [0,31,60,91,121,152,182,213,244,274,305,335,366]
    days_since = 0

    if year == 1901:
        days_since = days_in_months[month-1]+day-1
    else:
        for y in range(1901,year):
            if is_leap(y):
                days_since = days_since + 366
            else:
                days_since = days_since + 365

        if is_leap(year):
            days_since = days_since  + days_in_months_leap[month-1]+day-1
        else:
            days_since = days_since + days_in_months[month-1]+day-1

    return days_since

# Create a function to find the day of the week of the given date.
def day_of_the_week(day, month, year):

    how_many_days = days_since(day, month, year)


    if how_many_days%7 == 0:
        day = "Tuesday"
    elif how_many_days%7 == 1:
        day = "Wednesday"
    elif how_many_days%7 == 2:
        day = "Thursday"
    elif how_many_days%7 == 3:
        day = "Friday"
    elif how_many_days%7 == 4:
        day = "Saturday"
    elif how_many_days%7 == 5:
        day = "Sunday"
    elif how_many_days%7 == 6:
        day = "Monday"

    print(day)

day_of_the_week(1, 3, 2016)


#Q3

def take_integral(A,x1,x2):

    A.reverse()
    integral_list = [0]*len(A)

    for i in range(0,len(A)):
        eval_x1 = A[i]*(x1)**(i+1)/(i+1)
        eval_x2 = A[i]*(x2)**(i+1)/(i+1)
        integral_list[i] = eval_x2 - eval_x1

    integral = round(sum(integral_list),2)
    return integral


print(take_integral([1, 2, 1], 0, 3))
print(take_integral([5, 0, 0, -2, 1], 0, 1))
