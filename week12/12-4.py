import math
class Box1:
    def __init__(self,shape='s',length=0,width=0,height=0,radius=0):
        self.shape = shape
        self.length = length
        self.height = height
        self.width = width
        self.radius = radius
    def perimeter(self):
        if self.shape == 'r':
            return (self.length + self.width)*2
        elif self.shape == 's':
            return self.length*4
        elif self.shape == 't':
            return self.length + self.width + (self.length**2 + self.width**2)**0.5
        else:
            return math.pi * self.radius * 2
    def area(self):
        if self.shape == 'r':
            return self.length * self.width
        elif self.shape == 's':
            return self.length**2
        elif self.shape == 't':
            return self.length * self.width / 2.0
        else:
            return math.pi * self.radius ** 2
        
height = int(input("height"))
width = int(input("width"))
length = int(input("length"))
shape = input("what shape is it")
radius= int(input("radius"))
yash1 = Box1(shape,length,width,height,radius)
print("perimeter",yash1.perimeter())
print("area",yash1.area())
