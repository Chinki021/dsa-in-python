--link : https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1

# Approach:
# 1. Create a frequency map (dictionary) to store the count of each element.
# 2. Traverse the array and update the frequency of every number.
# 3. Create a result array.
# 4. For each number from 1 to n:
# - If the number exists in the frequency map, add its frequency.
# - Otherwise, add 0.
# 5. Return the result array
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def frequencyCount(self, arr):
        n=len(arr)
        
        freq={}
        
        for num in arr:
            freq[num]=freq.get(num,0)+1
            
        result=[]
            
        for i in range(1,n+1):
            result.append(freq.get(i,0))
        return result
