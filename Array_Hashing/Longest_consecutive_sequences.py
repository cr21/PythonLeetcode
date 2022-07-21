"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109


"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # TLE 69/72 case pass
#         s = set(nums)
#         max_count=0
#         for num in nums:
#             count=0
#             flag = True
#             while flag:
#                 if num in s:
#                     count+=1
#                     num+=1    
#                 else:
#                     flag=False
                    
#             max_count = max(max_count, count)
#             print("max_count", max_count, count)
            
#         return max_count
                    
        # optimized
        
        s = set(nums)
        max_count=0
        for num in nums:
            if (num-1) not in s:
                counter = 0
                while num in s:
                    counter+=1
                    num+=1
                max_count = max(max_count, counter)
                
        return max_count
                
