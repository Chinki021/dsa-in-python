--link : https://www.geeksforgeeks.org/problems/prime-number2314/1

# Approach:
# 1. Assume the number is prime initially.
# 2. Iterate through all numbers from 2 to n-1.
# 3. If any number divides n exactly, mark it as not prime.
# 4. Break the loop as soon as a divisor is found.
# 5. Return the result of the prime check.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isPrime(self, n):
        for i in range(2,n+1):
            isPrime=True
            
            for i in range(2,n):
                if n%i==0:
                    isPrime=False
                    break

            return isPrime
