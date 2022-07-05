"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
 

Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104



"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        ans = float("inf")
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            
            while left < right:
                s  = nums[left]+ nums[i] + nums[right]
                
                # sum is not equal to target
                # find diff
                diff = target-s
                
                
                if abs(diff) < abs(ans)   :
                    ans = diff
                if s < target:
                    left+=1
                else:
                    right-=1
            if ans == 0 :
                break
        return target-ans
