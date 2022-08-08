#we have anotherw way taht allow us to pass named arguments to a function this is called keyword arguments
#**kwargs
#kwargs is the name of the parameter and ** means it can accept any no of named value in the function
def student_report(**kwargs):
    total=0
    for k,v in kwargs.items():
        print(k,v)
        total+=v
    return len(kwargs),total/len(kwargs)

print(student_report(rohan=50,rani=80,ajay=20))
print(student_report(rani=90,raja=35,ajay=67,kumari=89))