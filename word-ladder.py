class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # O(n^2 * m) time,  O(n^2 * m) space
        # BFS Graph
        
        if endWord not in wordList:
            return 0
        
        adj = collections.defaultdict(list)
        wordList.append(beginWord)
        
        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] + '*' + w[j+1:]
                adj[pattern].append(w)
                
        visit = set([beginWord])
        q = collections.deque([beginWord])
        
        length = 1
        
        while q:
            for i in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return length
                else:
                    for j in range(len(w)):
                        pattern = w[:j] + '*' + w[j+1:]
                        for neigh in adj[pattern]:
                            if neigh not in visit:
                                visit.add(neigh)
                                q.append(neigh)
                        
            
            
            length+=1
            
        
        return 0
