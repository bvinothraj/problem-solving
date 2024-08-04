"""
https://www.hackerrank.com/challenges/pairs/problem?isFullScreen=true

Given an array of integers and a target value, determine the number of
pairs of array elements that have a difference equal to the target value.

Input:
k = 1
arr = [1,2,3,4]

Output: 3
Because of three pairs: [(2,1),(3,2),(4,3)]

2 <= n <= 10^5
0 < k < 10^9
0 < arr[i] < 2^31 - 1
each integer arr[i] will be unique

"""

import unittest

# pylint: disable=missing-docstring


class Solution:

    def get_pairs(self, arr, k):
        lookup = set(arr)
        pairs = []
        for item in arr:
            if item - k in lookup:
                pairs.append((item, item-k))

        return pairs


class TestSolution(unittest.TestCase):
    def test_get_pairs(self):
        items = [1, 2, 3, 4]
        k = 1
        expected = [(2, 1), (3, 2), (4, 3)]
        actual = Solution().get_pairs(items, k)
        self.assertListEqual(expected, actual)

    def test_get_pairs_no_pairs(self):
        items = [2, 7, 3, 8]
        k = 3
        expected = []
        actual = Solution().get_pairs(items, k)
        self.assertListEqual(expected, actual)

    def test_get_pairs_boundary(self):
        items = [2, 7, 3, 8]
        k = 6
        expected = [(8, 2)]
        actual = Solution().get_pairs(items, k)
        self.assertListEqual(expected, actual)

    def test_get_pairs_negative_diff(self):
        items = [2, 7, 3, 8]
        k = -5
        expected = [(2, 7), (3, 8)]
        actual = Solution().get_pairs(items, k)
        self.assertListEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
