class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def neighbors(node):
            for index in range(4):
                ele = int(node[index])
                # clock wise and anti clockwise
                for _dir in [1,-1]:
                    next_pos = (ele+_dir) % 10
                    # copy all element till index
                    # add clockwise or anticlockwise
                    # and copy rest of the element
                    yield node[:index]+str(next_pos)+node[index+1:]
        
        deadset = {i for i in deadends}
        queue = deque()
                                # string, depth
        queue = collections.deque([('0000', 0)])
        path_length =  0
        found = False
        visited={"0000"}
        
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            
            if node in deadset:
                continue
                
            for neigh in neighbors(node):
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append([neigh, depth+1])
        return -1
            
