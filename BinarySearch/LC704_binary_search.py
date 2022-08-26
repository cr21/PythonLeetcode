"""

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.


"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        left = 0
        
        right = len(nums)-1
        # iterative Binary Search Algorithm
        
        while left<= right:
            # pivot element
            mid = left + (right-left)//2
            
            # if current mid or pivot element is target 
            # return mid or pivot index
            if nums[mid]== target:
                return mid
            
            # if target is greater than mid 
            # change left pointer
            
            if nums[mid]< target:
                left = mid+1
            # if target is less than mid 
            # change right pointer 
            else:
                right = mid-1
        
        # if right and left pointer crosses each other and still you don't file solution
        # element is not in array
        return -1
                
            
