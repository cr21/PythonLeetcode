"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

"""

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0]*n
        right_max = [0]*n
        
        left_max[0] = height[0]
        right_max[n-1] = height[n-1]
        
        for index in range(1,n):
            left_max[index] = max(left_max[index-1], height[index])
            
        for index in range(n-2,-1,-1):
            right_max[index] = max(right_max[index+1], height[index])
            
        water = 0
        for index in range(n):
            current_allocation = min(right_max[index], left_max[index])-height[index]
            water +=current_allocation
            
        return water
      
      
    
    
    class Solution:
      def trap(self, height: List[int]) -> int: 
          if not height: return 0

          l, r = 0, len(height) - 1
          leftMax, rightMax = height[l], height[r]
          res = 0
          while l < r:
              if leftMax < rightMax:
                  l += 1
                  leftMax = max(leftMax, height[l])
                  res += leftMax - height[l]
              else:
                  r -= 1
                  rightMax = max(rightMax, height[r])
                  res += rightMax - height[r]
          return res
