class MinStack:
    
    # O(1) time O(n) space

    def __init__(self):
        self.stack = []
        self.minVal = inf
        

    def push(self, val: int) -> None:
        if self.stack:
            prevVal, prevMin = self.stack[-1]
            self.stack.append([val, min(prevVal, prevMin)])
        else:
            self.stack.append([val, val])
            self.minVal = val
        self.minVal = min(self.minVal, val)

    def pop(self) -> None:
        prevVal, prevMin = self.stack.pop()
        self.minVal = prevMin
        
        

    def top(self) -> int:
        prevVal, prevMin = self.stack[-1]
        return prevVal
        

    def getMin(self) -> int:
        return self.minVal
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
