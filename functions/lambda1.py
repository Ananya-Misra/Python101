f=lambda x:x+3*5
g=lambda x,y:x**2+y**2

print(f(2))
print(f(4))
print(g(2,3))
print(g(f(2),f(4)))