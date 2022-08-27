"""

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1
"""

# 

class Solution:
    def isHappy(self, n: int) -> bool:
        
        # we get back to 1 
        # we get stuck in cycle
        # we keeps getting higher and higher number
        
        
        def get_next(n):
            
            num = 0
            
            while n  >0 :
                n, rem = (n // 10, n % 10)
                num += rem**2
                
            return num
        
        
        seen = set()
        
        # if we ever encounter next_num 
        # we can not get to 1 and we have cycle
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
            
            
            
        return n==1
            
