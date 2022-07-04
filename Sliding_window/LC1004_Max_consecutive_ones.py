"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # APPROACH 1 : My Solution
        left = 0
        right = 0
        counter = 0
        res = 0
        
        while right < len(nums):
            
            current_window_length = right- left+1
            
            if nums[right]==1:
                counter+=1
            else:
                # keep expanding window until we utilize all the k value    
                if k>0:
                    counter +=1
                    k-=1
                else:
                    # now we have all utilize flipping attempt
                    # its time to make some correction
                    counter+=1
                    k-=1 
                    # once K  is zero we can no longer flip zero to 1 to get max consecutive
                    # this is the time we need to shrink window and place left
                    # pointer to the position so that we still have 0 flipping attempt left
                    
                    while k !=0 :
                        # removing ones from window
                        if nums[left]==1:
                            counter-=1
                        else:
                            # if we are removing zero
                            # we have  more flip left
                            counter-=1
                            k+=1
                        left+=1
                        
            res = max(res, right-left+1)
            right+=1
        
        return res
        
        # My Solution eNDS
        
        # Apparoch 2 Elegant solution
        
        left = 0
        right = 0
        maxonesTillNow = 0
        onesCount = 0
        res  = 0 
        
        while right < len(nums):
            if(nums[right]==1):
                onesCount+=1
            maxonesTillNow = max(maxonesTillNow, onesCount)
            
            current_window_length = right - left +1
            
            # need to shrink the window
            if current_window_length - onesCount > k :
                if nums[left]==1:
                    onesCount-=1
                left+=1
                
            res = max(res, right-left+1)
            
            right+=1
            
        return res
            


  
