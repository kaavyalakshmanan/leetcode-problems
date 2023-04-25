class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # O(n) time O(n) space

        stack = []

        for t in tokens:
            if t not in {'+', '*', '-', '/'}:
                stack.append(int(t))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if t == '+':
                    stack.append(num2 + num1)
                elif t == '-':
                    stack.append(num2 - num1)
                elif t == '*':
                    stack.append(num2 * num1)
                else:
                    stack.append(int(num2/num1))
        
        return stack[0]

