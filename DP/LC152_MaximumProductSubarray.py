"""

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # BRUTEFORCE TRY EVERY SUBARRAY 
        # TLE 186/188 test case passed
        
#         if len(nums) == 0:
#             return 0
        
#         result  = nums[0]
        
#         for index in range(len(nums)):
#             product = 1
#             for j in range(index, len(nums)):
#                 product *= nums[j]
#                 result = max(result, product)
        
#         return result
    
        # optimized
        
        result = max(nums)
        curmin, curmax = 1,1
        
        # Maintain cur subarray max and min product
        for num in nums:
            # reset
            if num == 0:
                curmin, curmax = 1,1
                continue
                
            tmp=curmax*num
            curmax = max(curmin*num, curmax*num, num)
            curmin = min(curmin*num,tmp , num)
            
            
            result = max(result, curmax)
            
        return result
            
            
        
        
        
                
        
