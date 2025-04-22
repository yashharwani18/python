class Box1:
    def __init__(self,length,width,height):
        self.length = length
        self.height = height
        self.width = width
    def area(self):
        return self.length * self.width
    def volume(self):
        return self.length * self.height * self.width
height = int(input("height"))
width = int(input("width"))
length = int(input("length"))
yash1 = Box1(length,width,height)
print("area",yash1.area())
print("volume",yash1.volume())
