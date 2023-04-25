class MinStack:

    # O(1) time O(n) space
    # For this problem, we design our stack using a python stack, where push and pop and top are O(1) operations
    # However getMin is where we have to be creative
    # If every val we push to stack also contains the min so far (aka min of curr val and prev min), we can retrieve min in O(1) time

    def __init__(self):

        self.stack = []
        

    def push(self, val: int) -> None:

        if self.stack:
            prevMin = self.stack[-1][0]
            self.stack.append([min(prevMin, val), val])
        else:
            self.stack.append([val, val])
        

    def pop(self) -> None:

        self.stack.pop()
        

    def top(self) -> int:

        return self.stack[-1][1]

        

    def getMin(self) -> int:

        return self.stack[-1][0]


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
