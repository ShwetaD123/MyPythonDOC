
print('This is Prime Number')

def primeNumber(num):
    if num>1:
        for i in range(2,num//2):
            if num%i==0:
                print('NOT PRIME')
                break


        else:
            print('Prime')


    else:
        print('Not Prime')

primeNumber(1)