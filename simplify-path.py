class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # O(n) time O(n) space
        # Use a stack
        
        pathArr = path.split('/')
        currPath = []
        
        for curr in pathArr:
            if curr in {'', '.'}:
                continue
            if curr == '..':
                if currPath:
                    currPath.pop()
            else:
                currPath.append('/'+curr)
            
        return "".join(currPath) if currPath else "/"
            
            
