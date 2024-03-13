"""
LeetCode #58: Length of last word

Given a string s consisting of words and spaces, return the length of 
the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:

1 <= s.length <= 10^4
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

import unittest

# pylint: disable=missing-docstring

class Solution:

    def length_of_last_word(self, s: str) -> int:
        length = 0
        found = False
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                length += 1
                found = True
            elif found:
                break

        return length


class TestSolution(unittest.TestCase):
    def test_string_with_multi_words(self):
        s = "How are you doing"
        expected = 5
        solution = Solution()
        actual = solution.length_of_last_word(s)
        self.assertEqual(expected, actual)

    def test_edge_one_char_word(self):
        s = "H"
        expected = 1
        solution = Solution()
        actual = solution.length_of_last_word(s)
        self.assertEqual(expected, actual)

    def test_edge_one_char_word_with_space(self):
        s = "H  "
        expected = 1
        solution = Solution()
        actual = solution.length_of_last_word(s)
        self.assertEqual(expected, actual)

    def test_edge_multiple_words_with_more_spaces(self):
        s = "  How are   you  doing   "
        expected = 5
        solution = Solution()
        actual = solution.length_of_last_word(s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
