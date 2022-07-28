
#take alist of number from user in single input

numbers=list(map(int,input('>>>').split()))

print(numbers)

numbers_halfed=list(map(lambda i:int(i)/2,input('>>').split()))
print(numbers_halfed)
x=[1,2,3,34,2,43]
x_odd=list(filter(lambda i:i%2!=0,x))
print(x_odd)