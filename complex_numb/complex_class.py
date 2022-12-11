class Complex:

    def __init__(self,  real=None, imag=None):
        self.real = real
        self.imag = imag
    
    def __str__(self):
        return f"{self.real} + {self.imag}j"

    def __eq__(self, comp2):
        return str(self) == str(comp2)

    def __add__(self, comp2):
        return Complex(self.real + comp2.real, self.imag + comp2.imag)
    
    def __sub__ (self, comp2):
        return Complex(self.real - comp2.real, self.imag - comp2.imag)

    def __mul__ (self, comp2):
        return Complex(self.real*comp2.real - self.imag*comp2.imag, self.real*comp2.imag + comp2.real*self.imag)

    def  __truediv__ (self,comp2):
        return Complex((self.real * comp2.real + self.imag * comp2.imag) / (comp2.real ** 2 + comp2.imag ** 2),
                       (comp2.real * self.imag - self.real * comp2.imag) / (comp2.real ** 2 + comp2.imag ** 2))
    
    def __abs__ (self):
        return (self.real ** 2 + self.imag ** 2) ** (1 / 2)