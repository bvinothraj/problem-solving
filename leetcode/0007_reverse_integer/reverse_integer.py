"""
LeetCode #7: Reverse integer

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer 
range [-2^31, 2^31 - 1], then return 0.

"""

import unittest

# pylint: disable=missing-docstring


class Solution:
    def reverse_integer(self, num):
        INT_MIN, INT_MAX = -2**31, 2**32-1
        result = 0

        temp = abs(num)
        while temp > 0:
            ones_digit = temp % 10
            result = result*10 + ones_digit
            temp //= 10

        if result < INT_MIN or result > INT_MAX:
            return 0

        return result if num > 0 else -result


class TestSolution(unittest.TestCase):

    def test_reverse_integer_single_digit(self):
        sol = Solution()
        actual = sol.reverse_integer(2)
        expected = 2
        self.assertEqual(actual, expected)

    def test_reverse_integer_two_digit(self):
        sol = Solution()
        actual = sol.reverse_integer(12)
        expected = 21
        self.assertEqual(actual, expected)

    def test_reverse_integer_negative_number(self):
        sol = Solution()
        actual = sol.reverse_integer(-123)
        expected = -321
        self.assertEqual(actual, expected)

    def test_reverse_integer_largest_positive_number(self):
        sol = Solution()
        actual = sol.reverse_integer((2**31)-1)
        expected = 0
        self.assertEqual(actual, expected)

    def test_reverse_integer_smallest_negative_number(self):
        sol = Solution()
        actual = sol.reverse_integer(-(2**31))
        expected = 0
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
