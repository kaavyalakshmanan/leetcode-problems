class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        # use a stack
        # O(n) time O(n) space

        stack = [] # each item contains [char, count]

        for c in s:
            if stack and stack[-1][0] == c:
                stack.append([c, stack[-1][1]+1])

                if stack[-1][1] == k:
                    j = k
                    while j > 0:
                        stack.pop()
                        j-=1
            else:
                stack.append([c, 1])

        res = ""
        for c, count in stack:
            res += c
        return res
