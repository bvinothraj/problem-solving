"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get 
accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not 
equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums 
containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""

import unittest

# pylint: disable=missing-docstring

class Solution:
    def remove_element(self, nums, val):
        cur_pos = 0
        swap_pos = 0

        for cur_pos, item in enumerate(nums):
            if item != val:
                if cur_pos > swap_pos:
                    temp = item
                    item = nums[swap_pos]
                    nums[swap_pos] = temp

                swap_pos += 1

        return swap_pos

class TestSolution(unittest.TestCase):
    def test_val_not_in_list(self):
        nums = [2,3,3,2]
        val = 4
        expected = 4
        solution = Solution()
        actual = solution.remove_element(nums, val)
        self.assertEqual(expected, actual)

        for i in range(expected):
            self.assertNotEqual(nums[i], val)

    def test_val_in_list(self):
        nums = [2,3,3,2]
        val = 3
        expected = 2
        solution = Solution()
        actual = solution.remove_element(nums, val)
        self.assertEqual(expected, actual)

        for i in range(expected):
            self.assertNotEqual(nums[i], val)

    def test_edge_val_in_list_last_item(self):
        nums = [2,3,3,4]
        val = 4
        expected = 3
        solution = Solution()
        actual = solution.remove_element(nums, val)
        self.assertEqual(expected, actual)

        for i in range(expected):
            self.assertNotEqual(nums[i], val)

    def test_edge_val_in_list_first_item(self):
        nums = [4,3,3,2]
        val = 4
        expected = 3
        solution = Solution()
        actual = solution.remove_element(nums, val)
        self.assertEqual(expected, actual)

        for i in range(expected):
            self.assertNotEqual(nums[i], val)

    def test_edge_empty_list(self):
        nums = []
        val = 3
        expected = 0
        solution = Solution()
        actual = solution.remove_element(nums, val)
        self.assertEqual(expected, actual)

        for i in range(expected):
            self.assertNotEqual(nums[i], val)

    def test_edge_val_in_all_list(self):
        nums = [3,3,3,3,3,3]
        val = 3
        expected = 0
        solution = Solution()
        actual = solution.remove_element(nums, val)
        self.assertEqual(expected, actual)

        for i in range(expected):
            self.assertNotEqual(nums[i], val)

if __name__ == "__main__":
    unittest.main()
