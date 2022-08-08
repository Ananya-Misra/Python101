#generator are special functions in python
#that can be used to generate a sequence of values

print(range(1,10))
def cube(limit):
    for i in range(1,limit+1):
        yield i**3 #generate an output not display it

def fib(limit):
    a,b=0,1
    for i in range(limit,end='@ '):
        yield a
        a,b=b,a+b

def even(limit):
    for i in range(2,limit,2):
        yield i**2

for c in cube (10):
    print(c,sep='$ ')
for f in fib(15):
    print(f,sep='*',end='| ')

for e in even(19):
    print(e, end='$')

    