'''=========Fibonesis============(Ex of Geneartor)'''
'''
def feb():
    a,b=0,1
    while True:
        yield a
        a,b = b,a+b


for i in feb():
    if i>1000:
        break


    print(i)

'''

'''=============Iterator Example============================='''
'''
class Table :

    def __init__(self,num):
        self.num = num


    def __iter__(self):
        self.n = 0
        return self


    def __next__(self):

        if self.n < self.num *10 :
            res = self.n+self.num
            self.n +=self.num
            return res
        else:
            raise StopIteration




t = Table(10)
# op =t.__iter__()
# print(next(op))
op = iter(t)
for i in op :
    print(i)

'''
'''===========Iterator for power of numbers ======='''
'''
class Power :

    def __init__(self,num):
        self.num = num
        self.rs = 0

    def __iter__(self):
        self.n = 0
        return self



    def __next__(self):
        if self.n <= self.num :
                self.rs = self.n**2
                self.n+=1
                return self.rs
        else :
            raise StopIteration




Q = Power(5)
OP1=iter(Q)
print(next(OP1))
print(next(OP1))
# for i in OP1:
#     print(i)

'''

''' ==========Closure example=============================='''
'''

def outerFunction(msg):
    def Inner(msg2):
        res = (msg+' '+msg2)
        return (res)
    return Inner

ob1=outerFunction('Hiiii')
res=ob1('Shweta')
print(res)

ob2 = outerFunction('Goodmorning')
print(ob2(' Shweta'))
print(ob2(' Nita'))


del outerFunction

# ob3=outerFunction('m1')
# print(ob3('Noo'))


print(ob2('sdfg'))

'''

''' =========================Decorator=========================== '''
'''
def correctZeroError(func):
    def inner(x,y):
        if y!=0:
            return func(x,y)
        else:
            return 'We cannot devide this numbers'
    return inner



@correctZeroError
def multiply (x,y):

    return  x/y



print(multiply(12,3))

'''


'''=================Decorator=============================='''
'''
def checkavaibilityofFile(func):
    def inner(filepath):
        if filepath != ' ':
            return func(filepath)
        else:
             print('NO file is selected')
    return inner






@checkavaibilityofFile
def readfile(filepath):
    with open(filepath,'r') as f:
        res =f.readlines()
        print(res)



readfile('/home/ubantu/Downloads/info.txt')
# readfile( ' ')

'''


'''========Prime No .============='''
'''

def primeNumber(num):
    if num>0:
        for i  in range(2,num//2):
            if num%i == 0:
                return ('Not Prime')

        else:
            return ('Its a prime Number')

    else:
        return ('Not a prime number')


# print(primeNumber(13))


# def listPrimeNumber(list1):
#     for num in list1:
#         print(num)
#         if num>0:
#             for i  in range(2,num//2):
#                 if num%i == 0:
#                     return (num,'<-- Not Prime')
# 
#             else:
#                 return (num ,'<--Its a prime Number')
# 
#         else:
#             return (num,'<-- Not a prime number')
# 
# 
# print(listPrimeNumber([5,18,40,13]))


'''
'''==========check Palindrome of string===================='''
'''
s1 ='qwertrewq'
def palindrome(s1):
    if s1 == s1[::-1]:
        print('Its palindrome')
    else:
        print('Non palindrome')

palindrome(s1)

'''

'''================Palindrome of Number================================'''
'''
def numPalindrome(num):
    temp=num
    d =0
    while temp>0:
        digit=temp%10
        d=d*10 + digit
        temp = temp//10
    if d == num :
        print('palindrome')

    else:
        print('Non - Palindrome')

numPalindrome(128821)

'''

'''================Count digits of Number================================'''
'''
def countdigitnum(num):
    temp = num
    count = 0

    while temp>0:
        d=temp%10
        count+=1
        temp//=10

    print('Digits in num is:',count)


countdigitnum(12333)

'''

'''================ Armstrong Number ================================'''

'''
def armSTrong(num):

    temp =num
    n = len(str(num))
    sum = 0

    while temp>0:
        digit = temp%10
        sum+=digit**n
        temp//=10

    if num == sum:
        print('Armstrong Number')

    else:
        print('Not Armstrong Number')


armSTrong(1634)

'''

'''==============================factorial Function==========================='''
'''


def facto(num):
    fact = 1
    if num == 0:
        return 1

    fact = num * facto(num-1)

    return fact


print(facto(5))

'''

'''==============================Map Function to genreate square of list==========================='''

s1 = [1,2,3,4,5,6,7]
res = list(map(lambda n : n*n ,s1))
print(res)

'''==============================Lambda Function to perform expression==========================='''

op=lambda x,y :x+y*x
print(op(2,3))

'''==============================Filter Function to seperate even number ==========================='''
s1 = [1,2,3,4,5,6,7,8,9,10]
res = list(filter(lambda x:x%2==0,s1))
print(res)


'''==============================reduce Function to Add the list ==========================='''
import functools

m=functools.reduce(lambda x,y:x+y,s1)
print(m)








