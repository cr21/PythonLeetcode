"""
Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

FileSystem() Initializes the object of the system.
List<String> ls(String path)
If path is a file path, returns a list that only contains this file's name.
If path is a directory path, returns the list of file and directory names in this directory.
The answer should in lexicographic order.
void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
void addContentToFile(String filePath, String content)
If filePath does not exist, creates that file containing given content.
If filePath already exists, appends the given content to original content.
String readContentFromFile(String filePath) Returns the content in the file at filePath.
 

Example 1:


Input
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
Output
[null, [], null, null, ["a"], "hello"]

Explanation
FileSystem fileSystem = new FileSystem();
fileSystem.ls("/");                         // return []
fileSystem.mkdir("/a/b/c");
fileSystem.addContentToFile("/a/b/c/d", "hello");
fileSystem.ls("/");                         // return ["a"]
fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"
 

Constraints:

1 <= path.length, filePath.length <= 100
path and filePath are absolute paths which begin with '/' and do not end with '/' except that the path is just "/".
You can assume that all directory names and file names only contain lowercase letters, and the same names will not exist in the same directory.
You can assume that all operations will be passed valid parameters, and users will not attempt to retrieve file content or list a directory or file that does not exist.
1 <= content.length <= 50
At most 300 calls will be made to ls, mkdir, addContentToFile, and readContentFromFile.
"""


class File:
    
    def __init__(self):
        self.content=""
        # path name file dictionary
        self.files=dict()
        self.isFile = False
        
        
    
        

class FileSystem:

    def __init__(self):
        self.root = File()
        
         

    def ls(self, path: str) -> List[str]:
        
        ptr=self.root
        files=[]
        # if not root part
        if path != "/":
            
            splitter = path.split("/")
            # for each part check if it is already there
            # if it is there then go down to the tree
            # similart to Trie Data Structure
            for part in splitter[1:]:
                ptr = ptr.files[part]
            # if it is files
            if ptr.isFile:
                files.append(splitter[len(splitter)-1])
                return files
            
#         if root part directly return all files name
        res_files = list(ptr.files.keys())
        return sorted(res_files)
            
         

    def mkdir(self, path: str) -> None:
        ptr=self.root
        splitter = path.split("/")
        # create file if not exists already
        for part in splitter[1:]:
            if part not in ptr.files:
                ptr.files[part] = File()
            ptr = ptr.files[part]
                 

    def addContentToFile(self, filePath: str, content: str) -> None:
        ptr = self.root
        splitter= filePath.split("/")
        # recursively go to the second last part
        for part in (splitter[1:len(splitter)-1]):
            ptr = ptr.files[part]
        
        # check if last is in files or not, if not create and add content
        
        if splitter[len(splitter)-1] not in ptr.files:
            ptr.files[splitter[len(splitter)-1]] =File()
        ptr  = ptr.files[splitter[len(splitter)-1]]
        ptr.isFile=True
        ptr.content = ptr.content+content
        
        

    def readContentFromFile(self, filePath: str) -> str:
        
    
        # recursively go to the file and return content
        
        ptr = self.root
        splitter = filePath.split("/")
        for part in splitter[1:len(splitter) - 1]:
            ptr = ptr.files.get(part)
        return ptr.files[splitter[len(splitter) - 1]].content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
