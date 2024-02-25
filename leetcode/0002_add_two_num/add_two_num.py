"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

2 -> 4 -> 3
5 -> 6 -> 4

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

"""

import unittest


class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def add_two_num(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        res = dummy
        carry = 0

        while list1 or list2 or carry:
            sum = carry

            if list1:
                sum += list1.val
                list1 = list1.next

            if list2:
                sum += list2.val
                list2 = list2.next

            carry = sum//10
            sum %= 10
            dummy.next = ListNode(sum)
            dummy = dummy.next

        return res.next


class TestSolution(unittest.TestCase):
    def test1_add_two_num(self):
        """Simple test case."""
        l1_node3 = ListNode(3)
        l1_node2 = ListNode(4, l1_node3)
        list1 = ListNode(2, l1_node2)

        l2_node3 = ListNode(4)
        l2_node2 = ListNode(6, l2_node3)
        list2 = ListNode(5, l2_node2)

        solution = Solution()
        actual = solution.add_two_num(list1, list2)

        l3_node3 = ListNode(8)
        l3_node2 = ListNode(0, l3_node3)
        expected = ListNode(7, l3_node2)

        while expected:
            self.assertEqual(actual.val, expected.val)
            actual = actual.next
            expected = expected.next

    def test2_add_two_num(self):
        """Test case with carry."""
        l1_node3 = ListNode(7)
        l1_node2 = ListNode(4, l1_node3)
        list1 = ListNode(6, l1_node2)

        l2_node3 = ListNode(4)
        l2_node2 = ListNode(0, l2_node3)
        list2 = ListNode(5, l2_node2)

        solution = Solution()
        actual = solution.add_two_num(list1, list2)

        l3_node4 = ListNode(1)
        l3_node3 = ListNode(1, l3_node4)
        l3_node2 = ListNode(5, l3_node3)
        expected = ListNode(1, l3_node2)

        while expected:
            self.assertEqual(actual.val, expected.val)
            actual = actual.next
            expected = expected.next

    def test3_add_two_sum(self):
        """Edge case with single digit number."""
        list1 = ListNode(3)
        list2 = ListNode(4)
        expected = ListNode(7)

        solution = Solution()
        actual = solution.add_two_num(list1, list2)

        while expected:
            self.assertEqual(expected.val, actual.val)
            expected = expected.next
            actual = actual.next

    def test4_add_two_num(self):
        """Edge case with max value."""
        l1_node3 = ListNode(9)
        l1_node2 = ListNode(9, l1_node3)
        list1 = ListNode(9, l1_node2)

        l2_node3 = ListNode(9)
        l2_node2 = ListNode(9, l2_node3)
        list2 = ListNode(9, l2_node2)

        solution = Solution()
        actual = solution.add_two_num(list1, list2)

        l3_node4 = ListNode(1)
        l3_node3 = ListNode(9, l3_node4)
        l3_node2 = ListNode(9, l3_node3)
        expected = ListNode(8, l3_node2)

        while expected:
            self.assertEqual(actual.val, expected.val)
            actual = actual.next
            expected = expected.next


if __name__ == "__main__":
    unittest.main()
