-- link : https://www.naukri.com/code360/problems/number-of-digits_4538242

--Approach:
--Repeatedly divide the number by 10 until it becomes 0.
--Each division removes one digit and increments the count.
  
Time Complexity: O(log n)
Space Complexity: O(1)

--code

def countDigit(num):
   count=0
   while num>0:
      count+=1
      num=num//10
   return count
