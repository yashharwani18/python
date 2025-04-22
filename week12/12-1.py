class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __str__(self):
        return f"{self.real}+{self.imag}i"
    def add(self,other):
        return Complex(self.real+other.real,self.imag+other.imag)
    def sub(self,other):
        return Complex(self.real-other.real,self.imag-other.imag)
    def multiply(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)
    def divide(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real_part, imag_part)
a=Complex(4,5)
b=Complex(2,-3)
print(Complex.add(a,b))
print(Complex.sub(a,b))
print(Complex.multiply(a,b))
print(Complex.divide (a,b))
