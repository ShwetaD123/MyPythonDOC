
'''  With recurtion function '''



def fact(n):
    if n==1:
        return n


    else :
       return n*fact(n-1)


# print(fact(10))




'''  With IF Else statement '''

def facto(num):
    factorial = 1

    if num<0:
        print('Factoraial is not found for negative number :',num)


    elif num == 0:
        print(num,' Factorail is 1')


    else:

        for i in range(1,num+1):
            factorial=i*factorial
        print(factorial)

facto(0)