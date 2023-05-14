class TrieNode:

    # TrieNode class
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):

        self.root = TrieNode()
        

    # O(n) time O(n) space
    def insert(self, word: str) -> None:

        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.endOfWord = True

        
    # O(n) time
    def search(self, word: str) -> bool:

        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.endOfWord 
            
        
    # O(n) time
    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
