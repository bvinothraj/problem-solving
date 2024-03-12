"""
LeetCode #13: Roman to integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. 
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. 

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

import unittest

# pylint: disable=missing-docstring

class Solution:
    def roman_to_int(self, s: str):
        roman_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        for i, char in enumerate(s):
            next_value = roman_value[s[i+1]] if i < len(s)-1 else 0
            cur_value = roman_value[char]

            if cur_value < next_value:
                total -= cur_value
            else:
                total += cur_value

        return total


class Solution2:
    def roman_to_int(self, s: str):
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        prev_value = 0

        for c in reversed(s):
            cur_value = roman_values[c]
            if cur_value < prev_value:
                total -= cur_value
            else:
                total += cur_value
            prev_value = cur_value

        return total


class TestSolution(unittest.TestCase):
    def test_simple_one_symbol(self):
        s = "V"
        expected = 5
        solution = Solution()
        actual = solution.roman_to_int(s)
        self.assertEqual(expected, actual)

        solution2 = Solution2()
        actual = solution2.roman_to_int(s)
        self.assertEqual(expected, actual)

    def test_simple_two_symbols(self):
        s = "IV"
        expected = 4
        solution = Solution()
        actual = solution.roman_to_int(s)
        self.assertEqual(expected, actual)

        solution2 = Solution2()
        actual = solution2.roman_to_int(s)
        self.assertEqual(expected, actual)

    def test_all_same_symbols(self):
        s = "III"
        expected = 3
        solution = Solution()
        actual = solution.roman_to_int(s)
        self.assertEqual(expected, actual)

        solution2 = Solution2()
        actual = solution2.roman_to_int(s)
        self.assertEqual(expected, actual)

    def test_different_symbols(self):
        s = "LVIII"
        expected = 58
        solution = Solution()
        actual = solution.roman_to_int(s)
        self.assertEqual(expected, actual)

        solution2 = Solution2()
        actual = solution2.roman_to_int(s)
        self.assertEqual(expected, actual)

    def test_large_number(self):
        s = "MCMXCIV"
        expected = 1994
        solution = Solution()
        actual = solution.roman_to_int(s)
        self.assertEqual(expected, actual)

        solution2 = Solution2()
        actual = solution2.roman_to_int(s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
