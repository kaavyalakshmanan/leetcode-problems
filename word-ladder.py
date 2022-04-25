class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # For every word, we want at most 1 char difference
        # eg - hot
            # *ot, h*t, ho* --> possibilities 
        # Build adj list with key = pattern and val = list of words that fall into pattern (eg key = *ot val = [dot, hot])
        
        # O(n^2 * m) time O(n^2 * m) space where n = len(wordList) and m = len(word)
        
        if endWord not in wordList:
            return 0
       
        adj = defaultdict(list)
        wordList.append(beginWord)
        
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                adj[pattern].append(word)
                
        visit = set(beginWord)
        q = collections.deque([beginWord])
        pathLen = 1
        
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return pathLen
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for p in adj[pattern]:
                        if p not in visit:
                            q.append(p)
                            visit.add(p)
                        
            pathLen+=1
            
        return 0
            
