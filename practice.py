
'''-----------------Iterator for Square functionality---------------------------------------------------'''
'''

class Square :

    def __init__(self,num):
        self.num = num


    def __iter__(self):
        self.n = 0
        return self


    def __next__(self):
        if self.n <=self.num :
            result = self.n **2
            self.n+=1
            return result
        else :
            raise StopIteration



t =Square(4)
li = iter(t)
print(next(li))
print(next(li))
print(next(li))
print(next(li))

print()

for i in li :
    print(i)


'''

''' -------------------------Iterator for Table functionality ---------------------------------- '''

'''
class Table :

    def __init__(self,num):

        self.num = num
        self.result = 0


    def __iter__(self):

        self.n = 1
        return  self



    def __next__(self):
        if self.result != self.num*10:
            if self.n <= self.num :
                self.result = self.n * self.num
                self.n += 1
                return self.result
        else:
            raise  StopIteration

t = Table(10)
val=iter(t)
for i in val :
    print(i)

'''

'''-----------------------------Iterator program --------------------------'''

class Fibonesis :

    def __init__(self,a,b):
        self.a = a
        self.b = b


    def __iter__(self):
        # self.max = 1019
        return self


    def __next__(self):
        # if self.b != self.max:
            self.a = self.a
            self.b = self.a + self.b
            return self.a



f=Fibonesis(0,1)
i=iter(f)
for z in i :
    if z  >= 10000:
        break
    print(z)
