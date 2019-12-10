
'''  With recurtion function '''



def fact(n):
    if n==1:
        return n


    else :
       return n*fact(n-1)


# print(fact(10))




'''  With IF Else statement '''
'''
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




a,b,c = 310,20,120


res =a if (a>b and a>c) else (b if (b>c) else c)
print("value is greater",res)


c = [310,20,120]
v=(reversed(c))
print(c)
print(v)
for i in v :
    print(i)




s1='shweta'
n=len(s1)
i=-1
# while i>=-n:
#     print(s1[i],end='')
#     i-=1
#

i=0
while i<n:
    print(s1[i],end='')
    i+=1
s1='shweta'
# for i in s1:
#     print(i,end='')
#
for i in s1[::-1]:
    print(i,end='')

# d={}
seq=('a','b','c')
r=dict.fromkeys(seq,[13])
# print(r)

d = {1: "one", 2: "three"}
d.setdefault(4,'three')
d[1]='FIve'
print(d)
print(d.items())
print(d.keys())
print(dict.values(d))
print(d.pop(2))
print(d)
d1={41:'FOur'}
d.update(d1)
print(d)

'''

s1 = {1,'f','4',8,'pp',67}
s = {10,'f','4','42',8,'pp'}
print(s1)
print(s.union(s1))
print(s.intersection(s1))
print(s1.difference(s))
print(s1)
print(s1.difference_update(s))
print(s1)
print(s1.discard(45))
print(s1.i)


