import unittest
from complex_class import Complex

class TestComplex(unittest.TestCase):
    
    def test_equal(self):
        first = Complex(2, 5)
        second = Complex(2, 5)
        self.assertEqual(first, second)
        
    def test_equal_img(self):
        first = Complex(2, 6)
        second = Complex(2, 5)
        self.assertNotEqual(first, second)  

    def test_str(self):
        self.assertEqual(str(Complex(3,2)), '3 + 2j')

    def test_add(self):
        comp1 = Complex(1,-5)
        comp2 = Complex(0,7)
        expected = Complex(1,2)
        self.assertEqual(str(comp1+comp2) , str(expected))
    
    def test_sub(self):
        comp1 = Complex(-1,-5)
        comp2 = Complex(0,7)
        expected = Complex(-1,-12)
        self.assertEqual(str(comp1-comp2) , str(expected))

    def test_mul(self):
        comp1 = Complex(2,3)
        comp2 = Complex(-1,1)
        expected = Complex(-5,-1)
        self.assertEqual(str(comp1*comp2) , str(expected))

    def test_truediv(self):
        comp1 = Complex(-2, 1)
        comp2 = Complex(1, -1)
        expected = Complex(-1.5, -0.5)
        self.assertEqual(str(comp1 / comp2) , str(expected))

    def test_modul(self):
        comp1 = Complex(-17, 0)
        expected1 = 17.0

        comp2 = Complex(0, -1)
        expected2 = 1.0

        comp3 = Complex(3, -4)
        expected3 = 5.0

        self.assertEqual(str(abs(comp1)) , str(expected1))
        self.assertEqual(str(abs(comp2)) , str(expected2))
        self.assertEqual(str(abs(comp3)) , str(expected3))

if __name__ == "__main__":
  unittest.main()