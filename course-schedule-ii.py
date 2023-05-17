class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Reminder: If there are any cycles, return empty list
        # This is a classic graph problem with O(V+E) time aka O(p+n) where p = prereqs and n = courses, aka edges and vertices
        # Since we return empty list if there is cycle, we need to keep track of current path in a cycles set to recognize when we detect a cycle

        # Step 1: Build adjacency list
        adj = {}
        for c in range(numCourses):
            adj[c] = []
        for c1, c2 in prerequisites:
            adj[c1].append(c2)

        # Step 2: initialize visit and cycle sets
        # visit will tell us if we have already visited that course, cycle will tell us if we have already visited that course as part of current path
        visit, cycle = set(), set()
        output = []

        # A course has 3 possible states:
            # 1. Visited --> Its already been added to output
            # 2. Visiting --> Course hasnt been added to output yet, but its on the current path and added to cycle
            # 3. Unvisited --> Course hasnt been added to output or cycle

        # Step 3: DFS algo
        def dfs(c):
            # Step 3a: Detect cycle
            if c in cycle:
                return False
            # Step 3b: if course has already been visited
            if c in visit:
                return True

            # Step 3c: add course to cycle and recurse
            cycle.add(c)
            for p in adj[c]:
                if not dfs(p):
                    return False
            
            # Step 3d: remove course from current path as we are done with current path, add to visit as we have visited course and its prereqs
            cycle.remove(c)
            visit.add(c)

            # Step 3e: since course has been visited, we can add to output
            output.append(c)
            return True

        # Step 4: Call DFS algo 
        for c in range(numCourses):
            if not dfs(c):
                return []

        return output

        # This is a topological sort algo
        
