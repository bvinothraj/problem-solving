"""
https://www.hackerrank.com/challenges/candies/problem

Alice is a kindergarten teacher. She wants to give some candies to the 
children in her class.  All the children sit in a line and each of them 
has a rating score according to his or her performance in the class.  
Alice wants to give at least 1 candy to each child. If two children sit 
next to each other, then the one with the higher rating must get more 
candies. Alice wants to minimize the total number of candies she must buy.

Example:
arr = [4,6,4,5,6,2]
She gives the students candy in the following minimal amounts
[1,2,1,2,3,1]
So total minimum candies = 10

"""

import unittest

# pylint: disable=missing-docstring


class Solution:
    def candies_count(self, scores):
        n = len(scores)
        left_to_right = [1] * n
        right_to_left = [1] * n

        # left to right
        for i in range(1, len(scores)):
            if scores[i] > scores[i-1]:
                left_to_right[i] = left_to_right[i-1] + 1

        # left to right
        for i in range(len(scores)-2, -1, -1):
            if scores[i] > scores[i+1]:
                right_to_left[i] = right_to_left[i+1] + 1

        candies_total = 0
        for i in range(n):
            candies_total += max(left_to_right[i], right_to_left[i])

        return candies_total


class TestSolution(unittest.TestCase):
    def test_candies_count_increasing(self):
        scores = [2, 3, 4]
        expected = sum([1, 2, 3])
        actual = Solution().candies_count(scores)
        self.assertEqual(expected, actual)

    def test_candies_count_decreasing(self):
        scores = [4, 3, 2]
        expected = sum([3, 2, 1])
        actual = Solution().candies_count(scores)
        self.assertEqual(expected, actual)

    def test_candies_count_mixed(self):
        scores = [2, 5, 7, 4, 3, 9]
        expected = sum([1, 2, 3, 2, 1, 2])
        actual = Solution().candies_count(scores)
        self.assertEqual(expected, actual)

    def test_candies_count_with_repetition(self):
        scores = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
        expected = sum([1, 2, 1, 2, 1, 2, 3, 4, 2, 1])
        actual = Solution().candies_count(scores)
        self.assertEqual(expected, actual)

    def test_candies_count_all_same_values(self):
        scores = [3, 3, 3, 3, 3]
        expected = sum([1, 1, 1, 1, 1])
        actual = Solution().candies_count(scores)
        self.assertEqual(expected, actual)

    def test_candies_count_some_same_values(self):
        scores = [1, 2, 2]
        expected = sum([1, 2, 1])
        actual = Solution().candies_count(scores)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
