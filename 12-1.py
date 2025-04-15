class Box1:
    def __init__(self,length,width):
        self.length = length
        #self.height = height
        self.width = width
    #def area(self):
        #return 2 * (self.length* self.height + self.height*self.width + self.width*self.length)
    #def area(self):
        #return self.length * self.width
    #def volume(self):
        #return self.length * self.height * self.width
class Box2(Box1):
    def __init__(self,length,width,height):
        #super().__init__(length,width)
        self.width = width
        self.height = height
        self.length = length
    def volume(self):
        return self.length * self.height * self.width
    def area(self):
        return self.length*self.width
 
height = int(input("height"))
width = int(input("width"))
length = int(input("length"))
yash1 = Box1(length,width)
yash2 = Box2(yash1.length,height,yash1.width)
print("area",yash2.area())
print("volume",yash2.volume())
        
