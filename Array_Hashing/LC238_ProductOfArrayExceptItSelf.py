"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # APPROACH 1 TWO ARRAY
        
#         left = [1]* len(nums)
#         right = [1]*len(nums)
        
#         for index in range(1, len(nums)):
#             left[index] = left[index-1] * nums[index-1]
            
#         for index in range(len(nums)-2,-1,-1):
#             right[index] = right[index+1]*nums[index+1]
        
        
#         result = []
        
#         for x,y in zip(left, right):
#             result.append(x*y)
#         return result
    
        # APPROACH 2 TWO ARRAY
        
        result = [1]*len(nums)
        
        for index in range(1, len(nums)):
            result[index] = result[index-1] * nums[index-1]
        
        
        right  =  1
        
        for index in range(len(nums)-1, -1,-1):
            result[index] = result[index]*right
            right = right*nums[index]
            
        return result
            
