"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # APPROACH 1
        # filter_s = "".join(list(map(lambda x: x.lower(), filter(lambda x: x.isalnum(), s))))
        # APPROACH 2
        filter_s = "".join([ch.lower() for ch in s if ch.isalnum()])
        
        return filter_s == filter_s[::-1]
      
      
      
class Solution {
    public boolean isPalindrome(String s) {
        
        String S = s.toLowerCase();
        
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<S.length();i++) {
            char c=S.charAt(i);
            if(Character.isDigit(c) || Character.isLetter(c)) {
                sb.append(c);
            }
        }
        
        String processed_str = sb.toString();
        
        return isPallindromic(processed_str);
        
    }
    
    private boolean isPallindromic(String s) {
        int l = 0;
        int r = s.length()-1;
        
        while(l<=r) {
            if(s.charAt(l) != s.charAt(r)) {
                return false;
            }
            l++;
            r--;
            
        }
        
        return true;
        
    }
}
