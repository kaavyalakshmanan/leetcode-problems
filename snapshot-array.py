class SnapshotArray:

    def __init__(self, length: int):
        
        self.snaps = []
        self.sets = {}
        

    def set(self, index: int, val: int) -> None:
        
        # O(1) time O(1) space
        
        self.sets[index] = val
        

    def snap(self) -> int:
        
        # O(n) time O(n) space
 
        self.snaps += [self.sets] 
        self.sets = {}
        return len(self.snaps) - 1
        

    def get(self, index: int, snap_id: int) -> int:
        
        # O(n) time O(1) space
        
        for i in range(snap_id, -1, -1):
            if index in self.snaps[i]:
                return self.snaps[i][index]
            
        return 0
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
