"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # O(N^2) 
        # TLE
        # iterate over every pair, maintain min_height, and update max_Area
#         max_area=0
#         for i in range(len(heights)):
#             min_height = float("inf")
#             for j in range(i, len(heights)):
#                 min_height = min(min_height, heights[j])
#                 width = j - i +1
                
#                 max_area = max(max_area, width *min_height)
                
#         return max_area
    
    # devide and conquer
    
      # TLE

#         def get_area_in_bar(heights, start, end):
#             if start > end:
#                 return 0
            
#             # find minmum index
#             min_index = start
#             for i in range(start, end+1):
#                 if heights[min_index] > heights[i]:
#                     min_index= i
                    
#             area_with_min_height_bar = heights[min_index]*(end-start+1)
            
#             area_left_to_minimum = get_area_in_bar(heights,min_index+1, end)
#             area_right_to_minimum = get_area_in_bar(heights,start, min_index-1)
            
#             return max(
#                         area_with_min_height_bar, 
#                        max(area_left_to_minimum,area_right_to_minimum)
#                       )
#         return get_area_in_bar(heights, 0, len(heights)-1)
    # STACK
        max_area = 0
        stack = deque()
        stack.append(-1)
        
        for index in range(len(heights)):
            # pop out the element if current height is less than top of stack
            
            while (stack[-1] != -1 and heights[stack[-1]] >= heights[index] ):
                current_height = heights[stack.pop()]
                current_width = index - stack[-1]-1
                
                max_area = max(max_area, current_width*current_height)
            stack.append(index)
            
        while stack[-1]!=-1:
            current_height = heights[stack.pop()]
            current_width = len(heights)-stack[-1]-1
            max_area = max(max_area, current_width*current_height)
        return max_area
            
            
                    
            
        
        
        
    
            
            
            
                
                
