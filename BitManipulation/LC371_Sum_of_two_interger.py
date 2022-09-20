"""

Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000
371. Sum of Two Integers
"""

class Solution {
    public int getSum(int a, int b) {
        
        while (b!=0) {
            // for carry to take over
            int temp = (a&b ) << 1;
            // sum operation
            a = a^b;
            b= temp;
        } 
        return a;
        
        
            
        
    }
}
