class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        # O(m) time O(m) space
        
        output = [0] * n
        
        stack = [] # (id, time)
        
        prevId, prevOp, prevTime = logs[0].split(":")
        prevTime, prevId = int(prevTime), int(prevId)
        stack.append((prevId, prevTime))
        for i in range(1, len(logs)):
            currId, currOp, currTime = logs[i].split(":")
            currTime, currId = int(currTime), int(currId)
            if currOp == "start" and prevOp == "start":
                exclTime = currTime - prevTime
                output[prevId] += exclTime
                stack.append((currId, currTime))
            elif currOp == "end" and prevOp == "start":
                exclTime = currTime - prevTime + 1
                output[currId]+=exclTime
                stack.pop()
            elif currOp == "end" and prevOp == "end":
                exclTime = currTime - prevTime
                output[currId]+=exclTime
                stack.pop()
            elif currOp == "start" and prevOp == "end":
                exclTime = currTime - prevTime - 1
                if stack:
                    prevId, prevTime = stack[-1]
                    output[prevId]+=exclTime
                stack.append((currId, currTime))
                
            prevId, prevOp, prevTime = currId, currOp, currTime
        
        return output 
