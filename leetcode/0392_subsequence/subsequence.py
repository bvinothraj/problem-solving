"""
LeetCode: 0392 Is Subsequence

https://leetcode.com/problems/is-subsequence/description/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

"""

import unittest

# pylint: disable=missing-docstring


class Solution:
    def is_subsequence(self, s, t):
        if not s:  # empty string is a subsequence
            return True

        s_index = 0
        for char in t:
            if s_index < len(s) and s[s_index] == char:
                s_index += 1

                if s_index == len(s):
                    return True

        return False


class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = "abc"
        t = "ahbgdc"
        expected = True
        result = Solution().is_subsequence(s, t)
        self.assertEqual(expected, result)

    def test_partial_match(self):
        s = "agx"
        t = "ahbgdc"
        expected = False
        result = Solution().is_subsequence(s, t)
        self.assertEqual(expected, result)

    def test_positive_complete_match(self):
        s = "fullmatch"
        t = "fullmatch"
        expected = True
        result = Solution().is_subsequence(s, t)
        self.assertEqual(expected, result)

    def test_boundary_single_char_positive(self):
        s = "m"
        t = "m"
        expected = True
        result = Solution().is_subsequence(s, t)
        self.assertEqual(expected, result)

    def test_boundary_empty_s(self):
        s = ""
        t = "somestring"
        expected = True
        result = Solution().is_subsequence(s, t)
        self.assertEqual(expected, result)

    def test_negative(self):
        s = "mmm"
        t = "ahbgdc"
        expected = False
        result = Solution().is_subsequence(s, t)
        self.assertEqual(expected, result)

    def test_negative_single_char(self):
        s = "m"
        t = "n"
        expected = False
        result = Solution().is_subsequence(s, t)
        self.assertEqual(expected, result)

    def test_negative_empty_t(self):
        s = "min"
        t = ""
        expected = False
        result = Solution().is_subsequence(s, t)
        self.assertEqual(expected, result)

    def test_negative_bigger_substring(self):
        s = "iamabigstring"
        t = "small"
        expected = False
        result = Solution().is_subsequence(s, t)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
