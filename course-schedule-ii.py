class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # O(V+E) time O(V+E) space
        # DFS
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            
            for neigh in adj[course]:
                if not dfs(neigh):
                    return False
            
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
            
        
        adj = { c: [] for c in range(numCourses) }
        for c1, c2 in prerequisites:
            adj[c1].append(c2)
        output = []               
        visit, cycle = set(), set()
            
        for key, val in adj.items():
            if key not in visit:
                if not dfs(key):
                    return []
                
        return output 
