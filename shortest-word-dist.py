class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        wordsMap = defaultdict(list)
        
        for i, word in enumerate(wordsDict):
            wordsMap[word].append(i)
            
        word1Pos = wordsMap[word1]
        word2Pos = wordsMap[word2]
        i, j = 0, 0
        minDist = inf
        
        while i < len(word1Pos) and j < len(word2Pos):
            
            minDist = min(minDist, abs(word1Pos[i]- word2Pos[j]))
            if word1Pos[i] < word2Pos[j]:
                i+=1
            else:
                j+=1
                
        return minDist
                
