"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).

 

Example 1:

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:

Input: dummy_input = [""]
Output: [""]
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] contains any possible characters out of 256 valid ASCII characters.

"""

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # ch ='U+FFFF'
        # return  ch.join([i for i in strs])
        # APPROACH 1
        s = ""
        for part in strs:
            s+=str(len(part)) + "#" + part
            
            
        return s
        
    

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # ch ='U+FFFF'
        # return s.split(ch)
        
        # APPROACH 2
        ans=[]
        i=0
        while i < len(s):
            j = i
            # keep on moving jth pointer until we find # sign which indicates we got 
            # length part
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            # j points to pound sign
            # j+1 will points to string to appended
            # j+1 : j+1+length will be current part
            extracted_part =  s[j+1:j+1+length]
            ans.append(extracted_part)
            # move i pointer to next digit starts
            i=j+1+length
            
        return ans
            
            
            
                
                
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
