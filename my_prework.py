#Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.
def hello_name(user_name):
    print('hello ' + user_name.title() + '!')
hello_name('Akunmaru')

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for X in range(100):
        if X %2 != 0:
            print(X, end= ' ')
first_odds()

#Quesrion 3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.
def max_num_in_list(a_list):
    max = a_list[0]
    for num in a_list:
        if num > max:
            max = num
    return max
num_list = [2, 400 , 5 , 30 , 200 , 9123 , 12 , 7 ]
print(max_num_in_list(num_list))

#Questioin 4
#Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
def is_leap_year(a_year):
    year = input('Enter a year and I will tell you if it is a leap year!\n')
    if int(year) % 4 == 0:
        return True
    elif int(year) % 400 == 0:
        return True
    else:
        return False
print(is_leap_year(a_year=" "))

#Questinon 5
#Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list) +1))
num_list = [2, 3, 1, 4, 5, 9]
print(is_consecutive(num_list))