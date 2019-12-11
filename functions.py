'''======================Lambda function==================='''

s=lambda x,y : x*y

print('Result of Lambda Function---->',s(2,3))


'''======================filter even numbers using lambda function==================='''
seq = [1,2,3,4,5,6,7,8,9,10,11,12]
result = list(filter(lambda x:x%2 == 0,seq))
print('Result of Filter Function---->',result)



'''======================Map function every elements to its cube==================='''
seq = [1,2,3,4,5,6,7,8,9,10,11,12]
result = list(map(lambda x:x**3 ,seq))
print('Result of Map Function---->',result)



'''======================Map function with two seq but of same length==================='''
seq = [1,2,3,4,5,6,7,8,9,10,11,12]
seq1 = [1,2,3,4,5,6,7,8,9,10,11,12]

result = list(map(lambda x,y:x+y ,seq,seq1))
print('Result of Map Function---->',result)



'''======================Reduce function==================='''
import functools

seq = [1,2,3,4,5,6,7,8,9,10,11,12]
result =functools.reduce(lambda x,y:x+y ,seq)
print('Result of Reduce Function---->',result)


