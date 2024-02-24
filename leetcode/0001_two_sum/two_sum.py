"""

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9

"""

from typing import List
import unittest


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_indices:
                return [num_indices[diff], i]
            num_indices[num] = i


class TestSolution(unittest.TestCase):
    def test_two_sum(self):
        solution = Solution()

        # simple case with postive integers
        nums1 = [2, 7, 11, 15]
        target1 = 9
        self.assertEqual(solution.two_sum(nums1, target1), [0, 1])

        # case with negative integers
        nums2 = [-4, -2, -8, -1]
        target2 = -3
        self.assertEqual(solution.two_sum(nums2, target2), [1, 3])

        # case with positive and negative integers
        nums3 = [-4, 2, 8, -1]
        target3 = 4
        self.assertEqual(solution.two_sum(nums3, target3), [0, 2])

        # edge case
        nums4 = [10**9, 10**9 - 1]
        target4 = 2*10**9 - 1
        self.assertEqual(solution.two_sum(nums4, target4), [0, 1])


if __name__ == "__main__":
    unittest.main()
