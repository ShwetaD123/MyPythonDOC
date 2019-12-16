
'''--------------------------FIBONESIS SERIES FOR N NUMBERS-------------------'''

def fibonesis ():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b


for n in fibonesis():
    print("---",n)
    if n>10:
        break
    print(n)

fibonesis()


