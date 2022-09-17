"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105


"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans=set()
        nums = sorted(nums)
        
        def helper(nums, ans, index):
            left = index+1
            right = len(nums)-1
            
            while left < right:
                _sum = nums[index]+nums[left]+nums[right]
                
                if _sum > 0:
                    right-=1
                elif _sum < 0:
                    left+=1
                else:
                    # sum == 0
                    l = sorted([nums[left], nums[right], nums[index]])
                    ans.add(tuple(l))
                    left+=1
                    right-=1
                    
                    while left < right and nums[left] ==nums[left-1]:
                        left+=1
                    
                    while left < right and nums[right] ==nums[right+1]:
                        right-=1
                        
                    
        i = 0
        
        while i < len(nums) and nums[i] <= 0:
            # uncommenting below line won't affect answer
            if(i == 0 or nums[i]!=nums[i-1]):
                helper(nums, ans, i)
                
            i+=1
            
        return ans
    
    
            
            
            
        
