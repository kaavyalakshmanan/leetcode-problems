class SparseVector:
    def __init__(self, nums: List[int]):
        
        # O(n) time O(L) space
        
        self.sparseArr = []
        for i, num in enumerate(nums):
            if num > 0:
                self.sparseArr.append((i, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        
        i, j = 0, 0
        res = 0
        while i < len(self.sparseArr) and j < len(vec.sparseArr):
            idxI, valI = self.sparseArr[i]
            idxJ, valJ = vec.sparseArr[j]
            if idxI == idxJ:
                res += (valI * valJ)
                i+=1
                j+=1
            elif idxI < idxJ:
                i+=1
            else:
                j+=1
                
        return res
                
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
