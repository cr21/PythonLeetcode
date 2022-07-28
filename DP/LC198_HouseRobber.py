"""

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400


"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1, rob2=0,0
        
        #[rob1,rob2,1,2,3,1]
        for num in nums:
            choose = rob1+num
            notchoose = rob2
            temp = max(choose, notchoose)
            rob1 = rob2
            rob2=temp
            
        return rob2
        
#         if not nums:
#             return 0
        
       
        
#         # recursive solution
#         def max_gain(index, memo):
            
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
#             choose =  nums[index] + max_gain(index-2,memo)
#             # if you decided not to rob current house
#             not_choose = max_gain(index-1, memo)
#             memo[index]= max(choose, not_choose)
#             return max(choose, not_choose)
        
        
#         return max_gain(len(nums)-1, {})
            
        
