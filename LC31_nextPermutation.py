"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=2:
            nums.reverse()
            return
        
        index = len(nums)-2
        # iterate over array from right to left 
        # find the first index where nums[index-1] > nums[index]
        
        while index >=0 and nums[index] >= nums[index+1]:
            index-=1
        
        # found first pair where nums[index-1] > nums[index]
        # now we found our candidate for the swap
        # now we will find the element at indexj  which is just greater than elment at index-1 
        # we will swap with that element at  nums[j] and num[index-1]
        
        if index>=0:
            j = len(nums)-1
            # find the index at which nums[j] > nums[index]
            while nums[j] <=nums[index]:
                j-=1
            
            
            # swap num[index-1] and nums[j]
            
            nums[index], nums[j] = nums[j], nums[index]
            
        # now reverse list after [index+1]
        print(nums)
        
        def reverseList(nums, start):
            left = start
            right = len(nums)-1
            while left<right:
                nums[left], nums[right] = nums[right],nums[left]
                left+=1
                right-=1
                  
            
        reverseList(nums, index+1)
        
        
        
        
        
        
            
       
            
            
