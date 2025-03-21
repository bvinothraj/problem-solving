"""
https://www.hackerrank.com/challenges/angry-children/problem?isFullScreen=true
"""

import unittest

# pylint: disable=missing-docstring


class Solution:
    def max_min(self, k, arr):
        arr.sort()

        min_value = float('inf')
        for i in range(len(arr)-k+1):
            min_value = min(min_value, arr[i+k-1]-arr[i])

        return min_value

    def max_min_2(self, k, arr):
        arr.sort()
        return arr[k-1] - arr[0]


class TestSolution(unittest.TestCase):
    def test_max_min_k_is_2(self):
        arr = [1, 4, 7, 2]
        k = 2
        expected = 1
        actual = Solution().max_min(k, arr)
        self.assertEqual(expected, actual)

    def test_max_min_k_is_3(self):
        arr = [10, 100, 300, 200, 1000, 20, 30]
        k = 3
        expected = 20
        actual = Solution().max_min(k, arr)
        self.assertEqual(expected, actual)

    def test_max_min_repetition_k_is_3(self):
        arr = [1, 2, 1, 2, 1]
        k = 2
        expected = 0
        actual = Solution().max_min(k, arr)
        self.assertEqual(expected, actual)

    def test_max_min_k_is_5_edge(self):
        arr = [15, 10, 5, 17, 24]
        k = 3
        expected = 7
        actual = Solution().max_min(k, arr)
        self.assertEqual(expected, actual)

    def test_max_min_k_is_5_big_nums(self):
        arr = [4504, 1520, 5857, 4094, 4157, 3902, 822, 6643, 2422, 7288,
               8245, 9948, 2822, 1784, 7802, 3142, 9739, 5629, 5413, 7232]
        k = 5
        expected = 1335
        actual = Solution().max_min(k, arr)
        self.assertEqual(expected, actual)

    def test_max_min_k_is_3_complex(self):
        arr = [100, 200, 300, 350, 400, 401, 402]
        k = 3
        expected = 2
        actual = Solution().max_min(k, arr)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
