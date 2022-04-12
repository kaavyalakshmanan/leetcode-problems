class WordDistance:

    def __init__(self, wordsDict: List[str]):
        
        # O(n) time O(n) space
        
        self.wordsMap = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.wordsMap[word].append(i)
            
       

    def shortest(self, word1: str, word2: str) -> int:
        
        # O(max(m,n)) time
        # O(max(m,n)) space
        
        word1Pos = self.wordsMap[word1]
        word2Pos = self.wordsMap[word2]
        i, j = 0, 0
        minDist = inf
        
        while i < len(word1Pos) and j < len(word2Pos):
            minDist = min(minDist, abs(word1Pos[i]- word2Pos[j]))
            if word1Pos[i] < word2Pos[j]:
                i+=1
            else:
                j+=1
                
        return minDist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
