"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        # APPROACH 1 TLE
#         for i in range(len(height)):
            
#             for j in range(i, len(height)):
#                 width = j-i
#                 h = min(height[i], height[j])
#                 max_water=max(max_water,h*width)
                
#         return max_water

        left = 0
        right = len(height)-1
        
        while left <= right:
            
            w = right-left
            h = min(height[right], height[left])
            max_water = max(max_water, h*w)
            
            if height[right]> height[left]:
                left+=1
            else:
                right-=1
                
        return max_water
