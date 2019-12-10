
'''========================== Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.===================='''
'''
# limit = 19
list1 = []
def primeNumbers(limit):
    for i in range(0,limit):
        if i>1:
            for x in range(2,i):
                if i % x == 0:
                    break

            else :
                list1.append(i)
    return print(list1)


primeNumbers(22)
'''

# ============================Write a function called show_stars(rows). If rows is 5, it should print the following:======================================
'''
n=5
for i in range (n+1):
    print(i*'*')

'''


# =========================Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit
# with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:
#        0 EVEN
# 		1 ODD
# 		2 EVEN
# 		3 ODD   =======================================================

'''
def identify (limit ):

    for i in range(limit):
        if i%2 == 0:
            print(i,'is Even number')

        else:
            print(i,'is Odd number')


identify(5)


'''


# ================================================Write a function called fizz_buzz that takes a number.============================================
#
#
'''
# If the number is divisible by 3, it should return “Fizz”.
# 		If it is divisible by 5, it should return “Buzz”.
# 		If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# 		Otherwise, it should return the same number.
#

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'

    elif num%3 == 0:
        return 'Fizz'
    elif num%5==0:
        return 'Buzz'


    else :
        return num


print(fizz_buzz(30))


'''
# =========================================== Write a function that returns the maximum of two numbers.==========================================

'''
def max(n1,n2):
    return n1 if (n1>n2) else n2

print(max(25,35))


'''

# ===================================Write a function for checking the speed of drivers. This function should have one parameter: speed.

# If speed is less than 70, it should print “Ok”.
# 		Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the
# 		total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# 		If the driver gets more than 12 points, the function should print: “License suspended”===========================================

'''
def speedDriver(speed):

    if speed <70:
        print('OK')

    else :
        res = speed-70
        pt=res/5
        if pt>12:
            print('License Suspended')
        else:
            print('Points is ',pt)


speedDriver(130)

'''