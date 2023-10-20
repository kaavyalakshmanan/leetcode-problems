class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # O(n) time O(n) space
        
        stack = []
        for i, t in enumerate(tokens):
            # number case
            if t not in {'+', '-', '*', '/'}:
                stack.append(int(t))
            else:
                secondNum = stack.pop()
                firstNum = stack.pop()
                if t == '+':
                    stack.append(firstNum + secondNum)
                elif t == '-':
                    stack.append(firstNum - secondNum)
                elif t == '*':
                    stack.append(firstNum * secondNum)
                else:
                    stack.append(int(firstNum / secondNum))

        return stack[0]
