import unittest
from multiply import numbers
from bizzBuzz import bizBuzz

class firstTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_multiply(self):
        self.assertEqual(numbers(3,4),12)

    def test_strings(self):
        self.assertEqual(numbers('a',3),'aaa')

    def test_bizzBuzz(self):
        self.assertEqual(bizBuzz(),[1, 2, 'bizz', 4, 'Buzz', 'bizz', 7, 8, 'bizz', 'Buzz', 11, 'bizz', 13, 14, 'bizzBuzz', 16, 17, 'bizz', 19, 'Buzz', 'bizz', 22, 23, 'bizz', 'Buzz', 26, 'bizz', 28, 29, 'bizzBuzz', 31, 32, 'bizz', 34, 'Buzz', 'bizz', 37, 38, 'bizz', 'Buzz', 41, 'bizz', 43, 44, 'bizzBuzz', 46, 47, 'bizz', 49, 'Buzz', 'bizz', 52, 53, 'bizz', 'Buzz', 56, 'bizz', 58, 59, 'bizzBuzz', 61, 62, 'bizz', 64, 'Buzz', 'bizz', 67, 68, 'bizz', 'Buzz', 71, 'bizz', 73, 74, 'bizzBuzz', 76, 77, 'bizz', 79, 'Buzz', 'bizz', 82, 83, 'bizz', 'Buzz', 86, 'bizz', 88, 89, 'bizzBuzz', 91, 92, 'bizz', 94, 'Buzz', 'bizz', 97, 98, 'bizz', 'Buzz'])



if __name__ == '__main__':
    unittest.main()
