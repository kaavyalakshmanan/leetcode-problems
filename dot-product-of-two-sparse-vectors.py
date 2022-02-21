class SparseVector:
    def __init__(self, nums: List[int]):
        
        # self.nonZeros = {}
        # for i, num in enumerate(nums):
        #     if num > 0:
        #         self.nonZeros[i] = num
        
        self.pairs = []
        for index, value in enumerate(nums):
            if value != 0:
                self.pairs.append([index, value])
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        
#         res = 0
#         for i, n in self.nonZeros.items():
#             if i in vec.nonZeros:
#                 res += n * vec.nonZeros[i]
                
#         return res

        
        result = 0
        p, q = 0, 0

        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                result += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1

        return result
        
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
