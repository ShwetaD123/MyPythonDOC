

def function(num,op):

    if num > 0 and op != None :

        if op == '+':
            print(num+num)
            return 'Addition =',num+num

        elif op == '-':
            print(num - num)
            return 'subtraction =', num - num

        elif op == '/':
            print(num / num)
            return 'division =', num / num



        elif op == '*':
            print(num * num)
            return 'Multiplication =', num * num


        else :
            return 'something went wrong'


print(function(8,'*'))

