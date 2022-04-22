class RandomizedSet:

    def __init__(self):
        
        # O(1) time O(n) space
        
        self.dict = {}
        self.nums = []
        

    def insert(self, val: int) -> bool:
        
        if val not in self.dict:
            self.dict[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        
        if val in self.dict:
            idx = self.dict[val]
            lastVal = self.nums[-1]
            self.nums[idx] = lastVal
            self.nums.pop()
            self.dict[lastVal] = idx
            del self.dict[val]
            return True
        return False
        

    def getRandom(self) -> int:
        
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
