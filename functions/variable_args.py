
#how many parameters in a function
#flexible in function
#that is called variable arguments
#we define a function with *args as parameter
#where args is the name of parameter


def multiplier(*numbers):
    out =1
    for val in numbers:
        out*=val
    return out
#call 
print(multiplier(2,3,4,5))
print(multiplier())
print(multiplier(2,3,4,5,6,7,8,9,10))