"""
LeetCode Problem 9: Palindrome number

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
Therefore it is not a palindrome.

"""

import unittest

# pylint: disable=missing-docstring

class Solution():
    def is_palindrome(self, num: int) -> bool:
        if num < 0:
            return False

        return num == self.reverse_num(num)

    def reverse_num(self, num: int) -> int:
        temp = abs(num)
        reversed_num = 0

        while temp:
            rem = temp % 10
            temp = temp // 10
            reversed_num = (reversed_num * 10) + rem

        if num < 0:
            return -reversed_num

        return reversed_num


class TestSolution(unittest.TestCase):
    def test_simple_case(self):
        solution = Solution()
        value = 123
        self.assertFalse(solution.is_palindrome(value))

    def test_large_number(self):
        value = 123456789
        solution = Solution()
        self.assertFalse(solution.is_palindrome(value))

    def test_edge_single_digit(self):
        value = 9
        solution = Solution()
        self.assertTrue(solution.is_palindrome(value))

    def test_edge_trailing_zeroes(self):
        value = 123000
        solution = Solution()
        self.assertFalse(solution.is_palindrome(value))

    def test_edge_negative_number(self):
        value = -121
        solution = Solution()
        self.assertFalse(solution.is_palindrome(value))

    def test1_reverse_num(self):
        """Simple test case."""
        solution = Solution()
        value = 123
        expected = 321
        actual = solution.reverse_num(value)
        self.assertEqual(expected, actual)

    def test2_reverse_num(self):
        """Test case for large number."""
        value = 123456789
        expected = 987654321
        solution = Solution()
        actual = solution.reverse_num(value)
        self.assertEqual(expected, actual)

    def test3_reverse_num(self):
        """Edge case with single digit."""
        value = 9
        expected = 9
        solution = Solution()
        actual = solution.reverse_num(value)
        self.assertEqual(expected, actual)

    def test4_reverse_num(self):
        """Edge case with trailing zeroes."""
        value = 123000
        expected = 321
        solution = Solution()
        actual = solution.reverse_num(value)
        self.assertEqual(expected, actual)

    def test5_reverse_num(self):
        """Test case with negative number"""
        value = -234
        expected = -432
        solution = Solution()
        actual = solution.reverse_num(value)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
