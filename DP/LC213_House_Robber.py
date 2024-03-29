"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        if len(nums)==1:
            return nums[0]
        
        # APPROACH 1
#         def max_gain(index, memo, nums):
            
#             if index < 0:
#                 return 0
            
#             if index in memo:
#                 return memo[index]
            
#             if index == 0 :
#                 memo[0] = nums[0]
#                 return nums[0]
            
#             if index == 1:
#                 memo[1] = max(nums[0], nums[1])
#                 return max(nums[0], nums[1])
            
#             # if you choose at current index, you could not have choosen to rob on previous index
#             choose =  nums[index] + max_gain(index-2,memo,nums)
#             # if you decided not to rob current house
#             not_choose = max_gain(index-1, memo,nums)
#             memo[index]= max(choose, not_choose)
#             return max(choose, not_choose)
        
        
        
#         # If we don't rob house 1
#         not_house1= max_gain(len(nums[1:])-1, {},nums[1:])
#         not_house_n = max_gain(len(nums[:-1])-1, {},nums[:-1])
#         # If we only have one element 
#         return  max(not_house1,not_house_n)

        def helper(nums):

            rob1, rob2=0,0

            #[rob1,rob2,1,2,3,1]
            for num in nums:
                choose = rob1+num
                notchoose = rob2
                temp = max(choose, notchoose)
                rob1 = rob2
                rob2=temp

            return rob2
        
        not_house1 =  helper(nums[1:])
        not_house_n = helper(nums[:-1])
        return max(not_house1, not_house_n)
        
        
