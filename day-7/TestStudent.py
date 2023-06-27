import unittest
import Student as std

class TestStudent(unittest.TestCase):

    # tear down methods
    def setUp(self):
        self.s1 = std.Student("Ali", 15 ,80)
        self.s2 = std.Student("Hassan", 12 ,70)

    def tearDown(self):
        pass

    def testEmail(self):
        self.assertEqual(self.s1.email , "Ali.15@gmail.com")
        self.assertEqual(self.s2.email, "Hassan.12@gmail.com")

    def testRaise(self):
        self.s1.applyRaise
        self.s2.applyRaise

        self.assertEqual(self.s1.grade, 88)
        self.assertEqual(self.s2.grade, 77)
