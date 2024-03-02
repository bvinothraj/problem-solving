"""
LeetCode Problem 14: Longest common prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

import unittest
from typing import List

# pylint: disable=missing-docstring

class Solution:
    def longest_common_prefix(self, strs: List[str]):
        min_len = min(len(item) for item in strs)

        common_prefix = ""
        for i in range(min_len):
            char = strs[0][i]
            if all(char == str[i] for str in strs):
                common_prefix += char
            else:
                break

        return common_prefix


class TestSolution(unittest.TestCase):
    def test_positive_case(self):
        strs = ["flower", "flow", "flight"]
        expected = "fl"
        solution = Solution()
        actual = solution.longest_common_prefix(strs)
        self.assertEqual(expected, actual)

    def test_negative_case(self):
        strs = ["dog", "racecar", "car"]
        expected = ""
        solution = Solution()
        actual = solution.longest_common_prefix(strs)
        self.assertEqual(expected, actual)

    def test_edge_empty_string(self):
        strs = ["", "racecar", "car"]
        expected = ""
        solution = Solution()
        actual = solution.longest_common_prefix(strs)
        self.assertEqual(expected, actual)

    def test_edge_matching_all_chars(self):
        strs = ["hello", "hello", "hello"]
        expected = "hello"
        solution = Solution()
        actual = solution.longest_common_prefix(strs)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
