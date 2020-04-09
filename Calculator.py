class calculator:
    def add (x,y):
        a = x+y
        print (a)
    def minus (x,y):
        b = x-y
        print (b)
    def multi (x,y):
        c = x*y
        print (c)
    def divide (x,y):
        b = x/y
        print (b)
    def square (x,y):
        b = x**y
        print (b)
    
a = float(input('Pehla number daal'))
b = float(input('Doosra number daal'))
z = input('kya krne ka h terko')

if z == 'add':
    calculator.add(a,b)
elif z == 'substract':
    calculator.minus(a,b)
elif z == 'multiply':
    calculator.multi(a,b)
elif z == 'divide':
    calculator.divide(a,b)
elif z == 'square':
    calculator.square(a,b)
else:
    print ('nikal pehli fursat mein')
