"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted,
you need to do the following things:

Change the array nums such that the first k elements of nums contain
the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.

Return k.

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation:
Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation:
Your function should return k = 5, with the first five elements of nums 
being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond the
returned k (hence they are underscores).

Constraints:

1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.

"""
from typing import List
import unittest

# pylint: disable=missing-docstring

class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        found_elems = {}
        swap_pos = 0
        cur_pos = 0

        for cur_pos, item in enumerate(nums):
            if item not in found_elems:
                if cur_pos > swap_pos:
                    nums[swap_pos], nums[cur_pos] = nums[cur_pos], nums[swap_pos]
                found_elems[item] = True
                swap_pos += 1

        return swap_pos


class TestSolution(unittest.TestCase):
    def test_multiple_duplicates(self):
        nums = [1,1,2,2,3,4,5]
        expected = 5
        expected_nums = [1,2,3,4,5]
        solution = Solution()
        actual = solution.remove_duplicates(nums)
        self.assertEqual(actual, expected)

        for i,item in enumerate(expected_nums):
            self.assertEqual(item, nums[i])

    def test_no_duplicates(self):
        nums = [1,2,3,4,5,6,7]
        expected = 7
        expected_nums = [1,2,3,4,5,6,7]
        solution = Solution()
        actual = solution.remove_duplicates(nums)
        self.assertEqual(actual, expected)

        for i,item in enumerate(expected_nums):
            self.assertEqual(item, nums[i])

    def test_edge_one_duplicate(self):
        nums = [1,1,3,4,5,6,7]
        expected = 6
        expected_nums = [1,3,4,5,6,7]
        solution = Solution()
        actual = solution.remove_duplicates(nums)
        self.assertEqual(actual, expected)

        for i,item in enumerate(expected_nums):
            self.assertEqual(item, nums[i])

if __name__ == "__main__":
    unittest.main()
