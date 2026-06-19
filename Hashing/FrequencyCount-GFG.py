--link : https://www.geeksforgeeks.org/problems/find-the-frequency/1
#since , GFG is asking for space complexity O(1) that's why this solution(this is brute force solution expected by GFG)

#Time Complexity  : O(n)
#Space Complexity : O(1)
# Approach:
# 1. Initialize a counter variable to 0.
# 2. Traverse the array.
# 3. If the current element equals x, increment the counter.
# 4. Return the final count
class Solution:
    def findFrequency(self,arr,x):
            count=0
            for num in arr:
                if num==x:
                    count+=1
            return count

  #otherwise the optimal solution is using hashing
# Approach:
# 1. Create a frequency map (dictionary).
# 2. Traverse the array and store the frequency of each element.
# 3. Return the frequency of x from the dictionary.
# 4. If x is not present, return 0

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def findFrequency(self,arr,x):
        freq={}
        
        for num in arr:
            freq[num]=freq.get(num,0)+1
        return freq.get(x,0)
