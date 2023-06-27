import unittest
import Calc as calc


class TestCalc(unittest.TestCase):
    def testAdd(self):
        result = calc.add(10,5)
        self.assertEqual(result,15)
        self.assertEqual(calc.add(20,4),24)

    def testSub(self):
        self.assertEqual(calc.subtract(20,5),15)
        self.assertEqual(calc.subtract(100,5),95)

    def testMul(self):
        self.assertEqual(calc.multiply(20, 5), 100)
        self.assertEqual(calc.multiply(25, 5), 125)

    def testDiv(self):
        self.assertEqual(calc.divide(20, 5), 4)
        self.assertEqual(calc.divide(20, 4), 5)
        self.assertNotEqual(calc.divide(-2, -2), -1)
        self.assertRaises(ValueError, calc.divide , 10, 0)
        # using context manager to test exceptions
        with self.assertRaises(ValueError):
            calc.divide(15,0)





if __name__ == "__main__":
    unittest.main()
