class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # classic dfs graph problem
        # O(n+p) time O(n) space
        # step 1: populate adjacency list
        adj = { i: [] for i in range(numCourses) }

        for c1, c2 in prerequisites:
            adj[c1].append(c2)

        visit = set()

        # step 2: dfs algo
        def dfs(c):
            if c in visit:
                return False
            if not adj[c]:
                return True

            visit.add(c)
            for p in adj[c]:
                if not dfs(p):
                    return False

            visit.remove(c)
            adj[c] = []
            return True

        for k, v in adj.items():
            if not dfs(k):
                return False

        return True
