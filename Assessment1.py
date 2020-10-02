#Assessment 1

#Q1
def my_function(x):
    input = int(x)
    my_list = [0,0,0]
    my_list[0] = input%3
    my_list[1] = input%5
    my_list[2] = input%7

    return my_list

print(my_function(165.1))

#Q2
def temp_convert(deg_far):
    deg_cel = round(5*(deg_far-32)/9,2)
    print(deg_cel)

temp_convert(45)

#Q3
def every_other_num(x1,x2):

    my_list = [x1]
    num = x1 + 2

    while num <= x2:
        my_list.append(num)
        num = num + 2

    return my_list

print(every_other_num(-7,26))

#Q4
def time_converter(milliseconds):

    # Insert your code here...
    years = int(milliseconds/31104000000)
    milliseconds = milliseconds-years*31104000000
    months = int(milliseconds/2592000000)
    milliseconds = milliseconds-months*2592000000
    days = int(milliseconds/86400000)
    milliseconds = milliseconds-days*86400000
    hours = int(milliseconds/3600000)
    milliseconds = milliseconds-hours*3600000
    mins = int(milliseconds/60000)
    milliseconds = milliseconds-mins*60000
    secs = int(milliseconds/1000)
    ms = milliseconds-secs*1000



    # Print the result
    print(f'{years} years,')
    print(f'{months} months,')
    print(f'{days} days,')
    print(f'{hours} hours,')
    print(f'{mins} minutes,')
    print(f'{secs} seconds,')
    print(f'and {ms} milliseconds.')

time_converter(1000000000)

int(3.822)
