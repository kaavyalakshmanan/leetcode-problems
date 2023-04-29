class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # O(nlogn) time O(n) space

        return self.mergeSort(nums)
        
        
    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        mid = ((0+len(nums)-1)//2)
        leftHalf = self.mergeSort(nums[:mid+1])
        rightHalf = self.mergeSort(nums[mid+1:])

        mergedArr = self.mergeArray(leftHalf, rightHalf)
        return mergedArr

    def mergeArray(self, leftArr: List[int], rightArr: List[int]) -> List[int]:
        res = [] 
        p1, p2 = 0, 0

        while p1 < len(leftArr) or p2 < len(rightArr):
            val1 = leftArr[p1] if p1 < len(leftArr) else inf
            val2 = rightArr[p2] if p2 < len(rightArr) else inf

            if val1 <= val2:
                res.append(val1)
                p1 += 1
            else:
                res.append(val2)
                p2 += 1

        return res


        
