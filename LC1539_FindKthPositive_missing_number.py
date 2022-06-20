"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length

"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        _min = arr[0]
        
        # if kth missing number is less than Arr[0]
        if (k <= arr[0]-1):
            return k
        # if not update how many number less than A[0] are missing and update K accordingly to search inside array
        k -=arr[0]-1
        
        for  i in range(len(arr)-1):
            # number of missing number curerently between two index
            curr_missing = arr[i+1]-arr[i]-1
            # if k is smaller than curr_missing return arr[i]+k
            if k <= curr_missing:
                return arr[i]+k
            # else update missing count reduction to k
            k-=curr_missing

        # if missing number is greater than array[-1]
        
        # if there are still missing number greater than arr[-1] return arr[-1]+k
        return arr[-1]+k
                
            
            
        
                
                
            
## Binary Search

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        left = 0
        right = len(arr)-1
        
        while left<=right:
            pivot = (right+left)//2
            
            # number of missing element less than arr[pivot]
            if arr[pivot]-pivot-1 < k:
                left = pivot+1
            else:
                right = pivot-1
        
        # # number of element before arr[right] should be subtracted from arr[right] and then we should add K to get the total count
        # at last left = right+1
        return left+k
        # return arr[right]+k - (arr[right]-right-1)
            
            
        
                
                
            

