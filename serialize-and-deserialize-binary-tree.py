# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    # O(n) time O(n) space

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def dfs(node):
            if not node:
                output.append("N")
                return
            output.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        output = []
        dfs(root)
        return ",".join(output)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        data = data.split(",")
        self.idx = 0
        
        def dfs():
            if data[self.idx] == "N":
                self.idx+=1
                return None
            root = TreeNode(int(data[self.idx]))
            self.idx+=1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
            
            
            
        
        
        
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
