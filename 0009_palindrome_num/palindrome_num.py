"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

"""

import unittest


class Solution():
    def is_palindrome(self, num: int) -> bool:
        if num < 0:
            return False

        return num == self.reverse_num(num)

    def reverse_num(self, num: int) -> int:
        temp = abs(num)
        reversed = 0

        while temp:
            rem = temp % 10
            temp = temp // 10
            reversed = (reversed * 10) + rem

        if num < 0:
            return -reversed

        return reversed


class TestSolution(unittest.TestCase):
    def test1_is_palindrome(self):
        """Simple test case."""
        solution = Solution()
        input = 123
        self.assertFalse(solution.is_palindrome(input))

    def test2_is_palindrome(self):
        """Test case for large number."""
        input = 123456789
        solution = Solution()
        self.assertFalse(solution.is_palindrome(input))

    def test3_is_palindrome(self):
        """Edge case with single digit."""
        input = 9
        solution = Solution()
        self.assertTrue(solution.is_palindrome(input))

    def test4_is_palindrome(self):
        """Edge case with trailing zeroes."""
        input = 123000
        solution = Solution()
        self.assertFalse(solution.is_palindrome(input))

    def test5_is_palindrome(self):
        """Test case with negative number"""
        input = -121
        solution = Solution()
        self.assertFalse(solution.is_palindrome(input))

    def test1_reverse_num(self):
        """Simple test case."""
        solution = Solution()
        input = 123
        expected = 321
        actual = solution.reverse_num(input)
        self.assertEqual(expected, actual)

    def test2_reverse_num(self):
        """Test case for large number."""
        input = 123456789
        expected = 987654321
        solution = Solution()
        actual = solution.reverse_num(input)
        self.assertEqual(expected, actual)

    def test3_reverse_num(self):
        """Edge case with single digit."""
        input = 9
        expected = 9
        solution = Solution()
        actual = solution.reverse_num(input)
        self.assertEqual(expected, actual)

    def test4_reverse_num(self):
        """Edge case with trailing zeroes."""
        input = 123000
        expected = 321
        solution = Solution()
        actual = solution.reverse_num(input)
        self.assertEqual(expected, actual)

    def test5_reverse_num(self):
        """Test case with negative number"""
        input = -234
        expected = -432
        solution = Solution()
        actual = solution.reverse_num(input)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
