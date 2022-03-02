class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        # O(R*C) time O(C) space
        # Reduce problem to largest rect in histogram
        
        def largestRectInHistogram(heights):
            stack = [] # (idx, height)
            maxArea = 0

            for i in range(len(heights)):
                currIdx, currHeight = i, heights[i]
                if not stack and currHeight == 0:
                    continue
                while stack:
                    prevIdx, prevHeight = stack[-1]
                    if currHeight < prevHeight:
                        maxArea = max(maxArea, (i - prevIdx) * prevHeight)
                        currIdx = prevIdx
                        stack.pop()
                    else:
                        break
                stack.append((currIdx, currHeight))

            i = len(heights)
            while stack:
                prevIdx, prevHeight = stack[-1]
                maxArea = max(maxArea, (i - prevIdx) * prevHeight)
                stack.pop()

            return maxArea
        
        # Step 1: Compute maxHeights
        
        ROWS, COLS = len(matrix), len(matrix[0])
        prevRow = [0] * len(matrix[0])
        maxArea = 0
        
        for row in range(ROWS):
            currRow = matrix[row]
            for col in range(COLS):
                currRow[col] = int(matrix[row][col])
                if row > 0:
                    prev, curr = prevRow[col], int(currRow[col])
                    if curr != 0:
                        currRow[col] = prev + curr 
            
            # Step 2: Find largest rect in histogram for current row
            
            largestRect = largestRectInHistogram(currRow)
            maxArea = max(maxArea, largestRect)
            prevRow = currRow
        
        return maxArea
                
        
