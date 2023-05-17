class TrieNode:
    def __init__(self, children: dict, endOfWord: bool):
        self.children = children
        self.endOfWord = endOfWord

    # Building TrieNode: O(n*m) where n = len(words) and m = len(word)
    # Space: O(n*m) space
    def addWord(self, word: str):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode({}, False)
            curr = curr.children[c]
        curr.endOfWord = True

# O(n*4^m) time O(n*m) space
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # If we treated this as a brute force DFS algo where we check every possible cell, it will be very inefficient.
        # If instead we used a Trie data structure, we can simultaneously check every character of every word in synch (aka check the 0th index of every word at the same time)

        # Step 1: Populate our trie data structure using above class definition
        root = TrieNode({}, False)
        for word in words:
            root.addWord(word)

        # Step 2: DFS algo but using prefix tree
        # takes in row, col, curr node, and word so far
        def dfs(row, col, curr, word):

            if row < 0 or row == rows or col < 0 or col == cols or (row, col) in visit or board[row][col] not in curr.children:
                return 

            visit.add((row, col))

            curr = curr.children[board[row][col]]
            word += board[row][col]
            if curr.endOfWord:
                res.add(word)

            dfs(row+1, col, curr, word)
            dfs(row-1, col, curr, word)
            dfs(row, col+1, curr, word)
            dfs(row, col-1, curr, word)

            visit.remove((row, col))


        rows, cols = len(board), len(board[0])
        # result set is to make sure there are no duplicates, visit set is to make sure we dont repeat (row, col) for a specific word search path, since we cant repeat the same char twice
        res, visit = set(), set()
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, "")

        return list(res)

        



