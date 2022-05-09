from typing import List
import unittest


def validBraces(braces_string: str):
    braces_stack: List[str] = []

    for brace in braces_string:
        if(brace == "(" or brace == "[" or brace == "{"):
            braces_stack.append(brace)
        elif(len(braces_stack) > 0):
            if(brace == ")" and braces_stack[-1] == "("):
                braces_stack.pop()
            elif(brace == "]" and braces_stack[-1] == "["):
                braces_stack.pop()
            elif(brace == "}" and braces_stack[-1] == "{"):
                braces_stack.pop()
        else:
            return False
    if(len(braces_stack) == 0):
        return True
    return False


def validBraces_v2(braces_string: str):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in braces_string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0


def validBraces_3(s: str):
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
    return s == ''


class TestStringMethods(unittest.TestCase):
    def test_empty_set(self):
        empty_input = ""
        self.assertEqual(validBraces(empty_input), True)
        self.assertEqual(validBraces_v2(empty_input), True)
        self.assertEqual(validBraces_3(empty_input), True)

    def test_valid_simple_braces(self):
        valid_simple_braces = "()"
        self.assertEqual(validBraces(valid_simple_braces), True)
        self.assertEqual(validBraces_v2(valid_simple_braces), True)
        self.assertEqual(validBraces_3(valid_simple_braces), True)

    def test_invalid_braces_set(self):
        invalid_braces_set = "[(])"
        self.assertEqual(validBraces(invalid_braces_set), False)
        self.assertEqual(validBraces_v2(invalid_braces_set), False)
        self.assertEqual(validBraces_3(invalid_braces_set), False)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
