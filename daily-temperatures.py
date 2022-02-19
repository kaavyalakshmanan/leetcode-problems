class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # O(n) time O(n) space
        # Use a stack
        
        output = [0] * (len(temperatures))
        stack = [(len(temperatures)-1, temperatures[-1])]
        
        
        for i in range(len(temperatures)-2, -1, -1):
            prevIdx, prevTemp = stack[-1]
            while temperatures[i] >= prevTemp:
                stack.pop()
                if not stack:
                    break
                prevIdx, prevTemp = stack[-1]
            if stack:
                output[i] = prevIdx - i
            stack.append((i, temperatures[i]))
            
        return output
