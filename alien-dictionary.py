class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        # O(c) time O(c) space
        # Topological Sort
        
        adjc = { c: set() for w in words for c in w }
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLength = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
                return ""
            for j in range(minLength):
                if w1[j] != w2[j]:
                    adjc[w1[j]].add(w2[j])
                    break
                    
        visit = {} # False = visited, True = curr path
        res = []
        
        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            for neigh in adjc[c]:
                if dfs(neigh):
                    return True
            visit[c] = False
            res.append(c)
            
        for c in adjc:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)
