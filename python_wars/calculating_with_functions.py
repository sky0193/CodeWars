"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:

    There must be a function for each number from 0 ("zero") to 9 ("nine")
    There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
    Each calculation consist of exactly one operation and two numbers
    The most outer function represents the left operand, the most inner function represents the right operand
    Division should be integer division. For example, this should return 2, not 2.666666...:

eight(divided_by(three()))
"""


def self(a): return a

def zero(f=self): return f(0)
def one(f=self): return f(1)
def two(f=self): return f(2)
def three(f=self): return f(3)
def four(f=self): return f(4)
def five(f=self): return f(5)
def six(f=self): return f(6)
def seven(f=self): return f(7)
def eight(f=self): return f(8)
def nine(f=self): return f(9)

# return lambda a: a + b
# returns a lambda function 
# for example if b = one() and plus
# it returns a:a + one()

def plus(b): return lambda a: a + b
def minus(b): return lambda a: a - b
def times(b): return lambda a: a * b
def divided_by(b): return lambda a: a // b

import unittest

class TestStringMethods(unittest.TestCase):
    def test_calculation(self):
        self.assertEqual(seven(times(five())), 35)
        self.assertEqual(four(plus(nine())), 13)
        self.assertEqual(eight(minus(three())), 5)
        self.assertEqual(six(divided_by(two())), 3)

def main():
    unittest.main()


if __name__ == '__main__':
    main()