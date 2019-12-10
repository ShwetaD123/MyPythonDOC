'''

def amstrong(num):
    temp = num
    n=len(str(num))
    print(n)
    sum = 0

    while temp>0:

        d1 = temp%10
        sum+=d1**n
        temp=temp//10

    if sum == num:
        print('Armstrong')

    else:
        print('Not Armstrong')


amstrong(54748)

'''
# Program to check Armstrong numbers in a certain interval


def amstrong(loweval,uppval):

    for num in range(loweval,uppval+1):
        temp = num
        n=len(str(num))
        sum = 0

        while temp>0:

            d1 = temp%10
            sum+=d1**n
            temp=temp//10

        if sum == num:
            print('Armstrong',num)

        # else:
        #     print('Not Armstrong',num)
        #

amstrong(100,66000)
