"""

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104

"""


# JAVA SOLUTION
# class Solution {
#     public int lengthOfLIS(int[] nums) {
    
        
#         List<Integer> sub = new ArrayList();
#         sub.add(nums[0]);
        
#         for(int i=1;i<nums.length;i++) {
            
            
#             if(nums[i] > sub.get(sub.size()-1) ) {
#                 sub.add(nums[i]);
#             }else{
#                 int j = binary_search(sub, nums[i]);
#                 sub.set(j, nums[i]);
#             }
            
            
#         }
        
#         return sub.size();     
#     }
    
#     private int binary_search(List<Integer> sub, int num) {
        
#         int left = 0;
#         int right =sub.size()-1;
        
#         int mid = (left+right)/2;
        
#         while(left < right) {
#             mid = (left+right)/2;
#             if(sub.get(mid)==num) {
#                 return mid;
#             }
            
#             if(sub.get(mid) < num) {
#                 left = mid+1;
#             }else{
#                 right=mid;
#             }
#         }
        
#         return left;
#     }
# }



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        LIS=[1]*len(nums)
        #iterate throuh array from back
        for i in range(len(nums)-1,-1,-1):
            # go through all the index till end of array
            # and see if you can make increasing subsequences out of it
            for j in range(i+1, len(nums)):
                if nums[i]< nums[j]:
                    LIS[i] =max(LIS[i], 1+ LIS[j])
        
        return max(LIS)
        
        
        
        
        
        
        
        
        
        
        
        
