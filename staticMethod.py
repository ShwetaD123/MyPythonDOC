
class Calculator:

    def multiplyNums(x, y):
        return x + y

# create addNumbers static method
Calculator.multiplyNums = staticmethod(Calculator.multiplyNums)

print('Product:', Calculator.multiplyNums(15, 110))



class Calculator:

    # create addNumbers static method
    @staticmethod
    def multiplyNums(x, y):
        return x + y

print('Product:', Calculator.multiplyNums(15, 110))

c1=Calculator.multiplyNums(20,50)
print('Sum :',c1)
