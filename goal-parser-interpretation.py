class Solution:
    def interpret(self, command: str) -> str:

        # O(n) time O(1) space

        i = 0
        res = ""
        while i < len(command):
            c = command[i]
            if c == 'G':
                res += c
            elif c == '(' and command[i+1] == ')':
                res += 'o'
                i+=1
            else:
                res += 'al'
                i += 3
            i+=1

        return res
