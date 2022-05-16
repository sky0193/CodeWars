"""
Define a function that takes one integer argument and returns logical value true or false depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Requirements

    You can assume you will be given an integer input.
    You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
    NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 (or similar, depends on language version). Looping all the way up to n, or n/2, will be too slow.

Example

is_prime(1)  /* false */
is_prime(2)  /* true  */
is_prime(-1) /* false */
"""
import math 
import unittest


def is_prime(num):
    if num == 2: return True

    if ((num < 2) or (num % 2 == 0)): 
        return False

    sqrt_num = math.floor(math.sqrt(num))
    for divisor in range(3, sqrt_num + 1, 2):
        if num % divisor == 0:
            return False
    return True


class TestStringMethods(unittest.TestCase):
    def test_not_prime(self):
        self.assertEqual(is_prime(-40), False)
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(9), False)
        self.assertEqual(is_prime(121), False)

    def test_prime(self):
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(5), True)


def main():
    unittest.main()


if __name__ == '__main__':
    main()