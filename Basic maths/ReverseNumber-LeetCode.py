--link : https://leetcode.com/problems/reverse-integer/
# Approach:
# 1. Store the sign of the number.
# 2. Convert the number to its absolute value.
# 3. Extract the last digit using modulo (% 10).
# 4. Append the digit to the reversed number using:
#       result = result * 10 + last_digit
# 5. Remove the last digit using integer division (// 10).
# 6. Repeat until the number becomes 0.
# 7. Restore the original sign and return the reversed number.

# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def reverse(self, n):
        sign = -1 if n<0 else 1
        n=abs(n)
        num=n
        result=0
        while num>0:
            last_digit=num%10
            result=result*10+last_digit
            num=num//10
        reult = sign * result
        if result < -(2**31) or result > (2**31 - 1):
            return 0

        return result
