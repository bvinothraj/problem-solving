"""
LeetCode #66: plus one

You are given a large integer represented as an integer array digits, where 
each digits[i] is the ith digit of the integer. The digits are ordered from 
most significant to least significant in left-to-right order. The large integer 
does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].


Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""

from typing import List
import unittest

# pylint: disable=missing-docstring


class Solution:
    def plus_one(self, num: List[int]) -> List[int]:
        result = []
        carry = 1

        for i in range(len(num)-1, -1, -1):
            digit_sum = num[i] + carry
            carry = digit_sum // 10
            result.append(digit_sum % 10)

        if carry:
            result.append(carry)

        result.reverse()

        return result


class TestSolution(unittest.TestCase):
    def test_number_without_carry(self):
        num = [1, 2, 3]
        expected = [1, 2, 4]
        solution = Solution()
        actual = solution.plus_one(num)
        self.assertListEqual(expected, actual)

    def test_number_with_carry(self):
        num = [1, 2, 9, 9]
        expected = [1, 3, 0, 0]
        solution = Solution()
        actual = solution.plus_one(num)
        self.assertListEqual(expected, actual)

    def test_edge_number_with_carry_single_digit(self):
        num = [9]
        expected = [1, 0]
        solution = Solution()
        actual = solution.plus_one(num)
        self.assertListEqual(expected, actual)

    def test_edge_number_with_carry_max_digit(self):
        num = [9, 9, 9, 9, 9, 9, 9, 9, 9]
        expected = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        solution = Solution()
        actual = solution.plus_one(num)
        self.assertListEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
