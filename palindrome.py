'''
def palindrome(n):
    temp = n
    rev = 0

    while temp>0:
        d=temp%10
        rev=rev*10+d
        temp //=10


    if n == rev:
        print('Palindrome')

    else:
        print('Non Palimdrome')

n=int(input('Enter Number:'))
palindrome(n)

'''
# for string


n1 =input('Enter a string: ')
rev = n1[::-1]

if n1 == rev:
    print('Palindrome')

else:
    print('Non Palimdrome')