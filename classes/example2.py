from turtle import color
from unicodedata import name


class Fruit:

    def __init__(self,name,color,size):
        self.name=name
        self.color=color
        self.size=size
    def __str__(self):
        return f'{self.name} is {self.color}'


#ever property and function is public by default i.e. directly accessible from the class :) :\ :( ;|
#inheritance
class Mango(Fruit):

    def __init__(self,name,color,size,variety):
        super().__init__(name,color,size)
        self.variety=variety
    def __str__(self):
        return f"{self.name} is {self.color} and {self.variety}"

if __name__=='__main__':
    f=Fruit('🍉','Green','Large')
    print(f)
    m=Mango('🥭','Yellow','small','Safeda')
    print(m)
    m2=Mango('🥭','Green','large','Langda')
    print(m2)