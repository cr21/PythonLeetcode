"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109

"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        if not piles:
            return -1
        
        if len(piles) > h :
            return -1
        # APPROACH 1 TRY every value :
        # TLE
#         k = 1
        
#         while True:
            
#             hours_count=0
            
            
#             for num in piles:
                
#                 hours_count+= math.ceil(num/k)
                
#             if hours_count <= h:
#                 return k
#             else:
#                 k+=1
                
        # APPROACH 2 BINARY SEARCH
        min_k = float("inf")
        left = 1
        right = max(piles)
        
        while left <= right:
            k = left + (right-left)//2
            
            hours_count = 0
            
            for num in piles:

                hours_count+= math.ceil(num/k)    
                
            if hours_count <= h:
                min_k = min(min_k, k)
                # if current k works let's try smaller value
                right = k-1
            else:
                left=k+1
                
        return min_k
                
                
            
