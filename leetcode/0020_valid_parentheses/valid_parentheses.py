"""
LeetCode Problem 20: Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false


Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""

import unittest

# pylint: disable=missing-docstring

class Solution:
    def valid_parentheses(self, expr: str) -> bool:
        stack = []
        parentheses = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        stack = []
        for char in expr:
            if char in parentheses:
                stack.append(char)
            elif char in parentheses.values():
                if not stack or parentheses[stack.pop()] != char:
                    return False

        return not stack


class TestSolution(unittest.TestCase):
    def test_simple_valid(self):
        value = "()"
        expected = True
        solution = Solution()
        actual = solution.valid_parentheses(value)
        self.assertEqual(expected, actual)

    def test_simple_valid_unnested(self):
        value = "()[]{}"
        expected = True
        solution = Solution()
        actual = solution.valid_parentheses(value)
        self.assertEqual(expected, actual)

    def test_simple_valid_nested(self):
        value = "{[()]}"
        expected = True
        solution = Solution()
        actual = solution.valid_parentheses(value)
        self.assertEqual(expected, actual)

    def test_simple_invalid(self):
        value = "(]"
        expected = False
        solution = Solution()
        actual = solution.valid_parentheses(value)
        self.assertEqual(expected, actual)

    def test_simple_invalid_nested(self):
        value = "([)]"
        expected = False
        solution = Solution()
        actual = solution.valid_parentheses(value)
        self.assertEqual(expected, actual)

    def test_edge_single_open_parenthesis(self):
        value = "("
        expected = False
        solution = Solution()
        actual = solution.valid_parentheses(value)
        self.assertEqual(expected, actual)

    def test_edge_single_closed_parenthesis(self):
        value = "}"
        expected = False
        solution = Solution()
        actual = solution.valid_parentheses(value)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
