--link : https://leetcode.com/problems/palindrome-number/
# Approach:
# Reverse the given number and compare it with the original number.
# If both are equal, the number is a palindrome.

# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, p):
        if p < 0:
            return False

        original = p
        result = 0

        while p > 0:
            last_digit = p % 10
            result = (result * 10) + last_digit
            p = p // 10

        return original == result
