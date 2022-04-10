class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        # O(n) time O(n) O(n) space
        
        stack = []
        time = -1
        output = [0] * n
        
        for log in logs:
            currLog = log.split(':')
            currId, currOp, currTime = int(currLog[0]), currLog[1], int(currLog[2])
            if currOp == 'end':
                currTime+=1
            if stack:
                prevId = stack[-1]
                output[prevId]+=(currTime-time)
            if currOp == 'start':
                stack.append(currId)
            else:
                stack.pop()
            time = currTime
                
        return output 
                
            
                
        
        
