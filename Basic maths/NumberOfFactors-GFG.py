--link : https://www.geeksforgeeks.org/problems/number-of-factors1435/1

--optimal solution

# Approach:
# 1. Iterate from 1 to root n.
# 2. If i divides n, then both i and (n // i) are factors.
# 3. Store both factors in a list.
# 4. Avoid duplicates when i == n // i (perfect square case).
# 5. Sort the list before returning.

# time complexity = O(sqrt root N)+O(N logN)
#space complexity = O(K)

from math import sqrt

class Solution:
    def countFactors(self, num):
        result = []

        for i in range(1, int(sqrt(num)) + 1):
            if num % i == 0:
                result.append(i)

                if num // i != i:
                    result.append(num // i)

        result.sort()
        return len(result)

  --better solution
# Approach:
# 1. Create an empty list to store factors.
# 2. Iterate from 1 to n/2.
# 3. If i divides n exactly (n % i == 0), then i is a factor.
# 4. Add the factor to the list.
# 5. After the loop, add n itself since every number is divisible by itself.
# 6. Return the list of factors.

# Time Complexity: O(n)
# Space Complexity: O(k)

class Solution:
    def countFactors (self, num):
        result=[]
        for i in range(1,(num//2) +1):
            if num%i==0:
                result.append(i)
        result.append(num)
        return len(result)
