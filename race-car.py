class Solution:
    def racecar(self, target: int) -> int:
        
        q = collections.deque([(0, 1, 0)])
        while q:
            pos, speed, length = q.popleft()
            if pos == target:
                return length
            q.append((pos+speed, speed*2, length+1))
            if speed > 0:
                if pos + speed > target:
                    q.append((pos, -1, length+1))
            else:
                if pos + speed < target:
                    q.append((pos, 1, length+1))
