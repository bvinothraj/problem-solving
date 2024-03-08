"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index where it 
would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
1 <= nums.length <= 10^4
-104 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""

from typing import List
import math
import unittest

# pylint: disable=missing-docstring

class Solution:
    def search_insert_position(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = right

        while left <= right:
            mid = math.ceil((left + right)/2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1

        return left


class TestSolution(unittest.TestCase):
    def test_target_found(self):
        nums = [1,5,8,11,15,20]
        target = 12
        expected = 4
        solution = Solution()
        actual = solution.search_insert_position(nums, target)
        self.assertEqual(expected, actual)

    def test_target_not_found(self):
        nums = [1,3,5,6]
        target = 2
        expected = 1
        solution = Solution()
        actual = solution.search_insert_position(nums, target)
        self.assertEqual(expected, actual)

    def test_edge_target_not_found_with_position_at_end(self):
        nums = [1,3,5,6]
        target = 8
        expected = 4
        solution = Solution()
        actual = solution.search_insert_position(nums, target)
        self.assertEqual(expected, actual)

    def test_edge_target_not_found_with_position_at_start(self):
        nums = [3,4,8,9]
        target = 2
        expected = 0
        solution = Solution()
        actual = solution.search_insert_position(nums, target)
        self.assertEqual(expected, actual)
    
    def test_edge_only_one_element_equal_to_target(self):
        nums = [3]
        target = 3
        expected = 0
        solution = Solution()
        actual = solution.search_insert_position(nums, target)
        self.assertEqual(expected, actual)

    def test_edge_only_one_element_less_than_target(self):
        nums = [3]
        target = 4
        expected = 1
        solution = Solution()
        actual = solution.search_insert_position(nums, target)
        self.assertEqual(expected, actual)
    
    def test_edge_only_one_element_greater_than_target(self):
        nums = [6]
        target = 4
        expected = 0
        solution = Solution()
        actual = solution.search_insert_position(nums, target)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
