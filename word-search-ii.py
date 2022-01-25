class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
        
    def searchWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        
        for word in words:
            root.addWord(word)
            
        ROWS, COLS = len(board), len(board[0])
        output, visited = set(), set()
        
        def dfs(row, col, node, word):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return
            if (row, col) in visited:
                return
            if board[row][col] not in node.children:
                return 
            
            visited.add((row, col))
            
            node = node.children[board[row][col]]
            word+=board[row][col]
            
            if node.endOfWord:
                output.add(word)
                
            dfs(row+1, col, node, word)
            dfs(row-1, col, node, word)
            dfs(row, col+1, node, word)
            dfs(row, col-1, node, word)
            
            visited.remove((row, col))
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
                
        return list(output)
                
                            
                
