"""
Given two strings needle and haystack, return the index of the first occurrence of 
needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:
1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.
"""

import unittest

# pylint: disable=missing-docstring

class Solution:
    """naive solution"""
    def index_of_first_occurrence(self, needle:str, haystack:str) ->int:
        index = -1
        npos = 0
        hpos = 0

        while hpos < len(haystack):
            if npos == len(needle):
                break
            if needle[npos] == haystack[hpos]:
                if index == -1:
                    index = hpos
                npos += 1
            elif index > -1:
                # partial match so reset and continue again
                index = -1
                npos = 0
                hpos -= 1

            hpos += 1

        # partial match at the end of haystack
        if npos < len(needle)-1:
            index = -1

        return index

class Solution2:
    """Sliding window technique"""
    def index_of_first_occurrence(self, needle: str, haystack: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)

        if needle_len == 0:
            return -1

        for i in range(haystack_len-needle_len + 1):
            if haystack[i:i+needle_len] == needle:
                return i

        return -1

class TestSolution(unittest.TestCase):
    def test_needle_found(self):
        needle = "low"
        haystack = "blow"
        expected = 1
        solution = Solution()
        actual = solution.index_of_first_occurrence(needle, haystack)
        self.assertEqual(expected, actual)

        solution2 = Solution2()
        actual = solution2.index_of_first_occurrence(needle, haystack)
        self.assertEqual(expected, actual)

    def test_needle_found_with_partial_match(self):
        needle = "low"
        haystack = "blolow"
        expected = 3
        solution = Solution()
        actual = solution.index_of_first_occurrence(needle, haystack)
        self.assertEqual(expected, actual)

        solution2 = Solution2()
        actual = solution2.index_of_first_occurrence(needle, haystack)
        self.assertEqual(expected, actual)

    def test_needle_found_with_multiple_match(self):
        needle = "low"
        haystack = "bllowlow"
        expected = 2
        solution = Solution()
        actual = solution.index_of_first_occurrence(needle, haystack)
        self.assertEqual(expected, actual)

        solution2 = Solution2()
        actual = solution2.index_of_first_occurrence(needle, haystack)
        self.assertEqual(expected, actual)

    def test_needle_haystack_same(self):
        needle = "blow"
        haystack = "blow"
        expected = 0
        solution = Solution()
        actual = solution.index_of_first_occurrence(needle, haystack)
        self.assertEqual(expected, actual)

        solution2 = Solution2()
        actual = solution2.index_of_first_occurrence(needle, haystack)
        self.assertEqual(expected, actual)

    def test_needle_not_found(self):
        needle = "fast"
        haystack = "quickblow"
        expected = -1
        solution = Solution()
        actual = solution.index_of_first_occurrence(needle, haystack)
        self.assertEqual(expected, actual)

        solution2 = Solution2()
        actual = solution2.index_of_first_occurrence(needle, haystack)
        self.assertEqual(expected, actual)

    def test_needle_empty(self):
        needle = ""
        haystack = "blow"
        expected = -1
        solution = Solution()
        actual = solution.index_of_first_occurrence(needle, haystack)
        self.assertEqual(expected, actual)

        solution2 = Solution2()
        actual = solution2.index_of_first_occurrence(needle, haystack)
        self.assertEqual(expected, actual)

    def test_edge_needle_haystack_single_char(self):
        needle = "a"
        haystack = "a"
        expected = 0
        solution = Solution()
        actual = solution.index_of_first_occurrence(needle, haystack)
        self.assertEqual(expected, actual)

        solution2 = Solution2()
        actual = solution2.index_of_first_occurrence(needle, haystack)
        self.assertEqual(expected, actual)

    def test_edge_needle_partial_match_at_haystack_end(self):
        needle = "lower"
        haystack = "fastblow"
        expected = -1
        solution = Solution()
        actual = solution.index_of_first_occurrence(needle, haystack)
        self.assertEqual(expected, actual)

        solution2 = Solution2()
        actual = solution2.index_of_first_occurrence(needle, haystack)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
