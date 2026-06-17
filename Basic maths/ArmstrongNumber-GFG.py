--link : https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1

# Approach:
# 1. Store the original number.
# 2. Count the number of digits in the number.
# 3. Extract each digit using modulo (% 10).
# 4. Raise the digit to the power of total digits.
# 5. Add the result to a running sum.
# 6. Compare the final sum with the original number.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def armstrongNumber (self, n):
        num=n
        total=0
        no_of_digits=len(str(n))
        while num>0:
            last_digit=num%10
            total=total + last_digit ** no_of_digits
            num=num//10
        return total==n
