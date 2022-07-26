def add(a,b,c=0,d=0):
  return a+b+c+d

if(__name__=='__main__'):
   print(add(a=10,c=20,d=10,b=30))
   print(add(a=10,b=20))
   print(add(20,20,c=10))
   print(add(20,d=23,c=10,b=30))