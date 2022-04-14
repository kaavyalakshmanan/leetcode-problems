class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        # O(n) time O(n) space
        
        def dfs(u):
            res.append(u)
            visit[u] = True
            
            for v in adj[u]:
                if not visit[v]:
                    dfs(v)
        
        adj = defaultdict(list)
        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)
            
        vertices = [ x for x in adj if len(adj[x]) == 1 ]
        visit = { x: False for x in adj }
        res = []
        dfs(vertices[0])
        return res
