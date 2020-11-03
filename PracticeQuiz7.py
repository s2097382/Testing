#Q1

def highest_integer():
    # Insert your code here
    n = 0
    lowest_m = False
    while (n+1)**2+6*(n+1)-3 < 3000:

        if not lowest_m:
            if n**2+6*n-3 > 500:
                lowest_m = True
                m = n

        n = n + 1


    # In the statments below, add the integers into the str() spaces.
    print("The highest integer n that satisfies n^2 + 6n - 3 < 3000 is "+str(n)+".")
    print("The lowest integer m that satisfies m^2 + 6m - 3 > 500 is "+str(m)+".")

highest_integer()

#Q2
def evens():
    num = 1
    while True:
        yield num*2
        num += 1


even_test = evens()
print(next(even_test))

#Q3

beverage_preference = {'Theo': 'coffee', 'Margaret': 'tea', 'Emily': 'tea', 'Fraser': 'coffee',
              'Jane': 'coffee', 'Peter': 'tea', 'Douglas': 'tea', 'Rodrigo': 'coffee',
              'Jennifer': 'tea', 'Abbie': 'coffee', 'Kyla': 'tea', 'Anna': 'coffee',
              'Katie': 'tea', 'Brian': 'coffee', 'Ian': 'coffee', 'Veronica': 'tea'}

def beverages():
    # Insert your code here.
    tea, coffee = [], []
    for name, beverage in beverage_preference.items():
        if beverage == 'tea':
            tea.append(name)
        else:
            coffee.append(name)

    tea.sort()
    coffee.sort()
    print(f'The tea drinkers are: {tea}')
    print(f'The coffee drinkers are: {coffee}')

beverages()

#Q4

def reverse_lookup(d,v):
    # Insert your code here
    my_list = []
    for key, val in d.items():
        if val == v:
            my_list.append(key)

    my_list.sort()
    return my_list

print(reverse_lookup({'h': 2, 'e': 3, 'l': 2, 'o': 1, 't': 1, 'r': 1}, 1))
print(reverse_lookup({'a': 6, 'r': 30, 'd': 12, 'v': 10, 'a': 11, 'r': 10}, 10))

#Q5

import statistics
def med_hw(x):
    l = len(x)
    h = []
    w = []
    for i in range(l):
        h.append(x[i][0])
        w.append(x[i][1])

    h.sort()
    w.sort()
    med_h = statistics.median(h)
    med_w = statistics.median(w)

    return (med_h,med_w)

a,b = med_hw([(1,2),(2,3),(3,4)])
print(abs(a-2)<1e-12 and abs(b-3)<1e-12)

#Q6

def student_res():
    '''
    Classify student results from the given dict in the way
    instructed.
    '''
    scores = {'s151': 41,'s152': 55,'s153': 82,'s154': 47,'s155': 35,'s156': 34,'s157': 64,'s158': 57,
          's159': 73, 's161': 82, 's162': 93, 's163': 54, 's164': 85, 's165': 16, 's166': 24}
    # Insert your code here.
    total_passed = 0
    firstyr_pass = 0
    secyr_pass = 0

    for num, score in scores.items():
        if score >= 40:
            total_passed = total_passed+1
            if num.startswith('s15'):
                secyr_pass = secyr_pass+1
            else:
                firstyr_pass = firstyr_pass+1

    total_passed = round(total_passed/15*100,2)
    secyr_pass = round(secyr_pass/9*100,2)
    firstyr_pass = round(firstyr_pass/6*100,2)
    return (total_passed,firstyr_pass,secyr_pass)

print(student_res())
