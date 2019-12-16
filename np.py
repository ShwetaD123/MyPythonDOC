import numpy as np

l1=[1,2,3,4,5,6]
result=np.array(l1)
print(result)
print(type(result))


''' -----------Mathematical operations with Array -----------------'''

print('Addition---->',result + 15)
print('Addition---->',result - 15)
print('Addition---->',result * 15)
print('Addition---->',result % 15)



'''------------------Shape of Array---------------------------------'''

M = np.array([1,2,3])
M1 = np.array([[1,2,3],[4,5,6]])  #-----------shape M1-- (2, 3)
M2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('shape--',M.shape)
print('shape M1--',M1.shape)
print('shape M2--',M2.shape)      #shape M2-- (3, 3)
print('dtype--',M.dtype)  #DataTYpe object

# shape-- (3,)
# dtype-- int64

M3 = np.array([[1,2.0,3],[4,5,6],[7,8,9]])
print('dtype -----',M3.dtype)   #-----dtype ----- float64   Dtype changes when value is float

'''-----------------------------DIMENSION Array--------------------------'''


a=np.array([
    [
        [1, 2,3],[4, 5, 6],[1,1,1]
    ],
    [
        [7, 8,9],[10, 11, 12],[1,1,1]
    ],
    [
        [7, 8,9],[10, 11, 12],[1,1,1]
    ]
]
)
print(a.shape)    #(3, 3, 3)  3 row column and ech conains 3 element



a1=np.array([
    [
        [1, 2,3],[4, 5, 6]
    ],
    [
        [7, 8,9],[10, 11, 12]
    ]
]
)
print(a1.shape)    #(2, 2, 3)  2 row and columns and contains 3 elements




a2=np.array([
    [
        [2,3],[4, 5, 6]
    ],
    [
        [7, 8,9],[11, 12]
    ]
]
)
print(a2.shape)    #(2, 2) 2 row and columns and elements are not same it will not define


'''-----------Single Line-----------------------------------'''

print(np.array([5,8,9]).shape)   #(3,)

'''---------------------------------np.zeros() and np.ones() commands------------------------------'''
#                   =====np.zeros()============

w=np.zeros((2,3,3),dtype=int)
# print(w)

# w = [[[0 0 0]
#       [0 0 0]
#       [0 0 0]]
#
#      [[0 0 0]
#       [0 0 0]
#       [0 0 0]]
#     ]



w2=np.zeros((3),dtype=int)
# print(w2)     #[0 0 0]



w1=np.zeros((3,2),dtype=int)
# print(w1)

# W =[[0 0]
#     [0 0]
#     [0 0]
#    ]


#  ==================np.ones() =======================

one=np.ones((1,2,3), dtype=np.int16)
# print('one --',one)

# one -- [
#         [
#             [1 1 1]
#             [1 1 1]
#         ]
#        ]


one1=np.zeros((2,2,3), dtype=np.float)
print(one1)

# [[[1. 1. 1.]
#   [1. 1. 1.]]
#
#  [[1. 1. 1.]
#   [1. 1. 1.]]]


'''--------------------------------Reshape Data ()----------------------------------------------------------------'''

rshape = np.array([[4,5,6],[1,2,3]])
print(rshape.shape)
# (2, 3)
print(rshape)

# [[4 5 6]
#  [1 2 3]]

print(rshape.reshape((3,1,2)))
# [[[4 5]]
#
#  [[6 1]]
#
#  [[2 3]]]

print(rshape.reshape((3,2)))

#OUTPUT OF RESHAPE
# [[4 5]
#  [6 1]
#  [2 3]]


'''--------------------------------Flatten Data ()----------------------------------------------------------------'''
flat =np.array([[4,5,6],[1,2,3],[9,6,3]])
print(flat.flatten())


# [4 5 6 1 2 3 9 6 3]



'''-----------------------------numpy.hstack() and numpy.vstack() in Python Example ------------------------------------------------'''


''' --( np.hstack )----------HORIZONTAL STACK =data can be append horizontically ----'''


f=np.array([1,2,3])
s=np.array([4,5,6])
print('Horizontal append ---->',np.hstack((f,s)))

# Horizontal append ----> [1 2 3 4 5 6]


''' ------( np.vstack )------Verticsl STACK =data can be append vertically ----'''


f1=np.array([1,2,3])
s1=np.array([4,5,6])
print('Vertical append ---->',np.vstack((f1,s1)))

# Vertical append ---->
# [[1 2 3]
#  [4 5 6]]



'''----------------------------Generate Random Numbers---------------------------------------------'''
normal_array = np.random.normal(5, 0.5, 10)
print(normal_array)



'''-------------------------------Asarray --- asarray--(to make the change in matrix values )---------------------------'''
a=np.zeros((4,4))
print(a)

# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

np.asarray(a)[3]=1
print(a)

# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [1. 1. 1. 1.]]



'''-----------Arrange-------------arrange to create values that are evenly spaced within a defined interval-----------------------------------'''

op=np.arange(1,11)
print(op)

# [ 1  2  3  4  5  6  7  8  9 10]

op1=np.arange(0,11,2)
print(op1)
# [ 0  2  4  6  8 10]



'''-----------------numpy.linespace(start,stop,num,endpoint)-----------------------------------'''

a=np.linspace(1,5,5,endpoint=False)   # If false stop value is not included
print(a)  #[1.  1.8 2.6 3.4 4.2]


a=np.linspace(1,5,5,endpoint=True)   # If false stop value is not included
print(a)  #[1. 2. 3. 4. 5.]



a=np.linspace(0,10,5,endpoint=True)   # If false stop value is not included
print(a)  #[ 0.   2.5  5.   7.5 10. ]


'''-----------------numpy.logspace(start,stop,num,endpoint)-----------------------------------'''
v=np.logspace(3.0, 4.0, num=4)	 # If false stop value is not included
print(v)
print(v.size)



x = np.array([1,2,3], dtype=np.complex128)
print(x.itemsize)
print(x.dtype)


'''============----------------------SLICING AND INDEXING-------------------------==========='''


import numpy as np
a = np.arange(10)
print('Arrange OP ---->',a)
s=slice(2,7,3)
print(a[s])



a = np.arange(10)
b = a[5]
print(b)


a = np.arange(10)
print (a[4:])


a = np.arange(10)
print (a[2:5])    #[2 3 4]

print()


a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print (a)

# [[1 2 3]
#  [3 4 5]
#  [4 5 6]]

print('------------Following code return the 2 column elements of entire Matrix--------')
print(a[...,2])   #[3 5 6]
print('------------Following code return the 2 Row of the Matrix--------')
print(a[2,...])   # [4 5 6]


# a1=np.arange(15)
# v=slice(2,8,2)
# print('***',a1[v])
# print(a1[6])
# print(a1[3:])
# print(a1[2:8:2])
# print()


import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0,1,2], [0,1,0]]   #It Will take elements from (0,0  --> 1  and (1,1) ---> 4 ,(2,0) --->5)
print (y)   #(1,4,5)


''' -------------Corners Of Matrix-----(4*3)--------------'''
print('\n')
a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])
print(a)


rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])

y=a[rows,cols]

print('-Corners Of Matrix-----(4*3)--',y)
print('\n')


'''----------Corners Of Matrix-----(3*3)----------'''

b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print('\n')
print(b)


r1 = np.array([[0,0],[2,2]])
c1 = np.array([[0,2],[0,2]])

y=b[r1,c1]

print('-Corners Of Matrix-----(4*3)--','\n',y)
print('\n')


'''------------------------------------------'''
import numpy as np 
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 

print('Our array is:' )
print(x )

# Our array is:
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]


print('\n')

'''-----------------------------slicing And Advanced Indexing ----------------'''
z = x[2:4,0:3]

print('After slicing, our array becomes:' )
print(z)
print('\n')

# After slicing, our array becomes:
# [[ 6  7  8]
#  [ 9 10 11]]

z = x[1:4,0:2]
print(z)

# After slicing, our array becomes:
# [[ 3  4]
#  [ 6  7]
#  [ 9 10]]


print('After slicing, our array becomes:' )
print(z)
print('\n')

# After slicing, our array becomes:
# [[ 4  5]
#  [ 7  8]
#  [10 11]]



z = x[2:4,2:3]

print('After slicing, our array becomes:' )
print(z)
print('\n')
#
# After slicing, our array becomes:
# [[ 8]
#  [11]]
#




'''---------------------Advanced Indexing---------------------'''
# using advanced index for column 
y = x[2:4,[0]]

print('Slicing using advanced index for column:')
print(y )
# Slicing using advanced index for column:
# [[6]
#  [9]]

print('\n')

y = x[1:4,[0,1]]

print('Slicing using advanced index for column:')
print(y )
# Slicing using advanced index for column:
# [[ 3  4]
#  [ 6  7]
#  [ 9 10]]
print('\n')


y = x[1:4,[1,2]]

print('Slicing using advanced index for column:')
print(y )

# Slicing using advanced index for column:
# [[ 4  5]
#  [ 7  8]
#  [10 11]]
print(''' ----- Boolean Array  ----''')
print(x[x>5])
# Boolean Array
# [ 6  7  8  9 10 11]


print('Boolean Array  -->')
print(x[x<6])  #[0 1 2 3 4 5]

print('\n')
''''''



import numpy as np
a = np.array([np.nan, 1,2,np.nan,3,4,5])
print(a[~np.isnan(a)])  #NaN (Not a Number) elements are omitted by using ~ (complement operator).
 # [1. 2. 3. 4. 5.]
 
 
'''--------------------Stastical Function--------------------------'''
 
import numpy as np 
a = np.array([[3,7,5],[8,4,3],[2,4,9]]) 

print('Our array is:' )
print(a )
print('\n' )

print( 'Applying amin() function:' )
print(np.amin(a,1) )
print( '\n'  )

print('Applying amin() function again:' )
print(np.amin(a,0)  )
print( '\n' )

print( 'Applying amax() function:' )
print(np.amax(a) )
print( '\n' )


print('Applying amax() function again:' )
print(np.amax(a, axis = 0) )
