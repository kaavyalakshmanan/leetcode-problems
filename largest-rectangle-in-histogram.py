class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # The way this algorithm works is, for every height we are comparing it to the height to the left
        # If height to left is smaller that currHeight, that means leftHeight can be extended to the right and we can keep going
        # Aka, add (idx, height) to stack
        # Otherwise, we keep popping from stack extending to the left, and updating current idx to be previous index
        # In other words, appending to stack = extending to the right
        # Popping from stack and updating currIdx to prevIdx = extending to the left
        # After this, at the end if stack is nonempty we have to keep popping and getting the areas

        # O(n) time O(n) space

        stack = []
        maxArea = 0

        for i in range(len(heights)):
            currIdx, currHeight = i, heights[i]
            while stack:
                prevIdx, prevHeight = stack[-1]
                if currHeight < prevHeight:
                    # The reason we dop i-prevIdx instead of currIdx-prevIdx is bc
                    # we want to get the area of the prev guy being extended to the right, which means we have to use i
                    maxArea = max(maxArea, (i-prevIdx) * prevHeight)
                    # But here, when we put in stack, we want to reinitialize currIdx because curr guy can be extended to the left
                    currIdx = prevIdx
                    stack.pop()
                else:
                    break

            stack.append((currIdx, currHeight))

        i = len(heights)
        while stack:
            prevIdx, prevHeight = stack[-1]
            maxArea = max(maxArea, (i-prevIdx) * prevHeight)
            stack.pop()

        return maxArea








        
