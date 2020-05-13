import unittest
from certifi import __main__


class Arithmetic(unittest.TestCase):
    def setUp(self):
        self.num1 = 10
        self.num2 = 20
        name = self.shortDescription()
        if name == "Add":
            self.num1 = 12
            self.num2 = 22
            print(self.num1, "  ", self.num2, " ", name)
        elif name == "Sub":
            self.num1 = 17
            self.num2 = 13
            print(self.num1, " ", self.num2, " ", name)

    def tearDown(self):
        print("End of test case :: ", self.shortDescription())

    def testAdd(self):
        result = self.num1 + self.num2
        self.assertTrue(result == 30, "Addition is failure")

    def testSub(self):
        result = self.num1 - self.num2
        self.assertTrue(result == -10, "Subtraction is failure")


if __name__ == __main__:
    unittest.main()
