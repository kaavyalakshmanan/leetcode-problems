class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # O(N + E) time O(N + E) space
        # DFS
        
        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for neigh in adj[node]:
                if neigh == prev:
                    continue
                if not dfs(neigh, node):
                    return False
                
            return True
            
        
        if n == 0:
            return True
        
        adj = { i:[] for i in range(n) }
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        visit = set()
        return dfs(0, -1) and len(visit) == n
        
        
            
