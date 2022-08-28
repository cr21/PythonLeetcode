"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 3 dots in word for search queries.
At most 104 calls will be made to addWord and search.

"""

class TrieNode:
        
        def __init__(self):
            self.isWord=False
            self.children = {}
            
class WordDictionary:
    
    
    
    def __init__(self):
        
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        
        for ch in word:
            # current character is not present in children
            # create TrieNode at position
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        # mark current node as True Word
        node.isWord = True
        
            
    def dfs_helper(self, word, root):   
        for index, ch in enumerate(word):
            # if current char is not in current node's children
            if ch not in root.children:
                # check if the current char is "." which can match any character 
                # and keep on searching from next char
                if ch==".":
                    # match any character and then keeep on searching
                    for c in root.children:
                        # if search ever returns True
                        # return
                        if(self.dfs_helper(word[index+1:], root.children[c])):
                            return True
                    # if for each of the matches we never get answer
                    # word is not present
                    
                    return False
                else:
                    # for any other character than "."
                    return False
                
            else:
                
                root= root.children[ch]
            
        return root.isWord 

    def search(self, word: str) -> bool:
        node=self.root
        return self.dfs_helper(word, node)
    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
