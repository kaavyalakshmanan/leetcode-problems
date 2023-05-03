class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        # O(n) time O(n) space

        dArray = list(dominoes)

        # we can use a queue to solve this problem
        q = collections.deque([])

        # initialize q with the indices of all the L's and R's in dominoes
        for i, c in enumerate(dArray):
            if c == "L" or c == "R":
                q.append(i)

        # keep going while q is non-empty
        while q:
            idx = q.popleft()
            nextIdx = -1
            if dArray[idx] == "L":
                if idx-1 >= 0 and dArray[idx-1] == ".":
                    nextIdx = idx-1

            # if R comes before L, a collission will happen
            # so we do the L check and then we pop the L from the q
            # but if L comes before R, there wont be a collision and we dont need to do a corresponding R check
            elif dArray[idx] == "R":
                if idx+1 < len(dArray) and dArray[idx+1] == ".":
                    nextIdx = idx+1
                if nextIdx != -1:
                    if nextIdx+1 < len(dArray) and dArray[nextIdx+1] == "L":
                        nextIdx = -1
                        q.popleft()
            
            if nextIdx != -1:
                dArray[nextIdx] = dArray[idx]
                q.append(nextIdx)

        return "".join(dArray)


        
        
