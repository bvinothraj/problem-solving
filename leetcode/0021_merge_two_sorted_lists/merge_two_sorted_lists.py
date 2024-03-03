"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

1 -> 2 -> 4
1 -> 3 -> 4

1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 4

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2: 
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

import unittest

# pylint: disable=missing-docstring

class ListNode:
    def __init__(self, value=0, nxt=None) -> None:
        self.value = value
        self.nxt = nxt

    def __repr__(self) -> str:
        if self.nxt:
            return "Node values not equal"

class ListNodeMatcher:
    """Matcher class to assertEqual two lists"""

    def __init__(self, expected) -> None:
        self.expected = expected

    def __eq__(self, other) -> bool:
        first = self.expected
        while first and other:
            if first.value != other.value:
                raise ValueError(f"actual.value={first.value} != expected.value={other.value}")
            first = first.nxt
            other = other.nxt

        # Ensure both lists have same length
        return first is None and other is None

    def __repr__(self) -> str:
        return repr(self.expected)


class Solution:
    def merge_sorted_list(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy

        while list1 or list2:
            node = ListNode()

            if list1 and list2:
                if list1.value <= list2.value:
                    node.value = list1.value
                    list1 = list1.nxt
                else:
                    node.value = list2.value
                    list2 = list2.nxt
            elif list1:
                node.value = list1.value
                list1 = list1.nxt
            elif list2:
                node.value = list2.value
                list2 = list2.nxt

            current.nxt = node
            current = node

        return dummy.nxt

class TestSolution(unittest.TestCase):
    def test_two_equal_length_lists(self):
        list1 = self.create_list([1,2,4])
        list2 = self.create_list([1,3,4])
        expected = self.create_list([1,1,2,3,4,4])

        solution = Solution()
        actual = solution.merge_sorted_list(list1, list2)
        self.assertEqual(ListNodeMatcher(actual), expected)

    def test_two_nonequal_length_lists(self):
        list1 = self.create_list([1,2,4])
        list2 = self.create_list([3,5,9,10])
        expected = self.create_list([1,2,3,4,5,9,10])

        solution = Solution()
        actual = solution.merge_sorted_list(list1, list2)
        self.assertEqual(ListNodeMatcher(actual), expected)

    def test_edge_two_empty_lists(self):
        list1 = self.create_list([])
        list2 = self.create_list([])
        expected = self.create_list([])

        solution = Solution()
        actual = solution.merge_sorted_list(list1, list2)
        self.assertEqual(ListNodeMatcher(actual), expected)

    def test_edge_one_empty_list(self):
        list1 = self.create_list([])
        list2 = self.create_list([-2])
        expected = self.create_list([-2])

        solution = Solution()
        actual = solution.merge_sorted_list(list1, list2)
        self.assertEqual(ListNodeMatcher(actual), expected)

    def create_list(self, items) -> ListNode:
        dummy = ListNode()
        current = dummy

        for item in items:
            node = ListNode(item)
            current.nxt = node
            current = node

        return dummy.nxt

if __name__ == "__main__":
    unittest.main()
