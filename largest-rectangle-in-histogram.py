class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # O(n) time O(n) space
        # Using stack
        
        stack = [] # (idx, height)
        maxArea = 0
        
        for i in range(len(heights)):
            currIdx, currHeight = i, heights[i]
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
