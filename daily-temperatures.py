class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # O(n) time O(n) space

        res = [0] * len(temperatures) 
        stack = [[temperatures[-1], len(temperatures)-1]]

        for i in range(len(temperatures)-2, -1, -1):
            # Stack has to remain monotonically decreasing
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1][1] - i
            stack.append([temperatures[i], i])

        return res
        
