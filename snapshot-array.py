class SnapshotArray:
    
    # O(n) time O(n) space

    def __init__(self, length: int):
        
        self.snaps = []
        self.sets = {}
        

    def set(self, index: int, val: int) -> None:
        
        self.sets[index] = val
        

    def snap(self) -> int:
        
        self.snaps += [self.sets]
        self.sets = {}
        return len(self.snaps)-1

    def get(self, index: int, snap_id: int) -> int:
        
        for i in range(snap_id, -1, -1):
            if index in self.snaps[i]:
                return self.snaps[i][index]
            
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
