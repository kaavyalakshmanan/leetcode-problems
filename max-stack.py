from collections import deque


class MaxStack(list):
    
    
    def __init__(self):
        self.stack = deque()
        self.peek = -float('inf')
    
    def push(self, x):
        
        self.peek = max(self.peek,x)    
        self.stack.append(x)
        
    def pop(self):
        
        m = self.stack.pop()
        if(m == self.peek):
            if(self.stack):
                self.peek = max(self.stack)
            else:
                self.peek = -float('inf')

        return m
        

    def top(self):
        
        return self.stack[-1]
        

    def peekMax(self):
        
        return self.peek
        

    def popMax(self):
        
        b = deque()
        while self.stack and self.stack[-1] != self.peek:
            b.append(self.stack.pop())
            
        self.stack.pop()
        
        while b:
            self.stack.append(b.pop())
        
        
        m = self.peek
        if(self.stack):
            self.peek = max(self.stack)
        else:
            self.peek = -float('inf')
            
        return m
            
