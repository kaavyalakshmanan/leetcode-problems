class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # O(N+E) time O(N+E) space
        # DFS
        
        def dfs(node, prev):
            visit.add(node)
            if not adj[node]:
                return 
            
            for neigh in adj[node]:
                if neigh == prev or neigh in visit:
                    continue
                dfs(neigh, node)
        
        adj = { i: [] for i in range(n) }
        visit = set()
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        numComponents = 0
        for node in adj:
            if node in visit:
                continue
            dfs(node, -1)
            numComponents+=1
            
        return numComponents
