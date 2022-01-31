class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # O(n+p) time O(n) space
        
        preMap = { i: [] for i in range(numCourses) }
        visited = set()
        
        # Initialize preMap
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
                
        # Check using DFS
        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            
            visited.add(course)
            for p in preMap[course]:
                if not dfs(p):
                    return False
            visited.remove(course)
            preMap[course] = []
            
            return True
        
        
        for course, p in prerequisites:
            if not dfs(course):
                return False
        
        return True
                
