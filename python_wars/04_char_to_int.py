"""
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
Example

alphabet_position("The sunset sets at twelve o' clock.")

Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )
"""
import string


def alphabet_position(text):
    result_str = ""
    a_int_prev = ord("a") - 1
    for char in text.lower():
        if char in string.ascii_letters:
            result_str += str(ord(char)-a_int_prev)
            result_str += " "
    return result_str[:-1]

def alphabet_position_comrehention(text):
    a_int_prev = ord("a") - 1
    return " ". join([str(ord(char)-a_int_prev) for char in text.lower() if char in string.ascii_letters])
    


import unittest

class TestStringMethods(unittest.TestCase):
    def test_calculation(self):
        self.assertEqual(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
        self.assertEqual(alphabet_position("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

        self.assertEqual(alphabet_position_comrehention("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")
        self.assertEqual(alphabet_position_comrehention("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")

def main():
    unittest.main()


if __name__ == '__main__':
    main()