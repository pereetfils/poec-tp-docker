import unittest
from calc import apply_vat


import unittest
"""
def apply_vat(price: float, percent: float):
    if isinstance(price , int):
        price = float(price)
    if isinstance(percent , int):
        percent = float(percent)
    if not isinstance(price , float):             
       raise ValueError(f'Price (${price}) is not a number')
    
    if price <= 0:
        raise ValueError(f'Price (${price}) is negative ou null')
    
    if percent < 0 or percent >100:
        raise ValueError(f'la TVA {percent}) est hors la loi ! out of range')
    
    return price * (1+percent/100)
"""
"""vous devez tester à minima que la fonction renvoie la bonne valeur pour :
price = 100, percent = 20,
price = 55.25, percent = 5.5,
price = 0, percent = 10,
price = -10.99, percent = 10,
price = 'wrong value', percent = 10
price = 100, percent = -10
price = 100, percent = 110"""

class Test_TVA(unittest.TestCase):
    def setUp(self):
        pass

    def test_test1(self):
        self.assertEqual(apply_vat(100, 20), 120)

    def test_test2(self):
        self.assertEqual(apply_vat(55.25, 5.5), 58.29)



        #self.assertEqual(apply_vat(0 , 10), 'ValueError: Price ($0.0) is negative ou null')
       # self.assertRaises()

    def test_test3(self):
        with self.assertRaises(ValueError):
            apply_vat(0 , 10)

    def test_test4(self):
        with self.assertRaises(ValueError):
            apply_vat(-10.99 , 10)

    def test_test4(self):
        with self.assertRaises(ValueError):
            apply_vat('wrong value' , 10)

    def test_test5(self):
        with self.assertRaises(ValueError):
            apply_vat(100 , -10)

    
    def test_test5(self):
        self.assertEqual(apply_vat('wrong value', 10), ValueError)
    def test_test5(self):
        self.assertEqual(apply_vat(100, -10), 'la TVA 110.0) est hors la loi ! out of range')

    def test_test5(self):
        self.assertEqual(apply_vat(100, 100), 200)


if __name__ == '__main__':
    unittest.main()