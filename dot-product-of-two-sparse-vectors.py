class SparseVector:
    def __init__(self, nums: List[int]):
        
        # O(n) time O(n) space
        
        self.arr = []
        for i, num in enumerate(nums):
            if num != 0:
                self.arr.append((i, num))
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        
        # O(min(m,n)) time O(1) space
        
        res = 0
        i, j = 0, 0
        
        while i < len(self.arr) and j < len(vec.arr):
            idx1, val1 = self.arr[i]
            idx2, val2 = vec.arr[j]
            if idx1 < idx2:
                i+=1
            elif idx2 < idx1:
                j+=1
            else:
                res += (val1 * val2)
                i+=1
                j+=1
                   
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
