class NumArray:

    # O(n) time O(n) space

    def __init__(self, nums: List[int]):

        self.prefixSums = [nums[0]]
        currSum = nums[0]
        for n in nums[1:]:
            currSum += n
            self.prefixSums.append(currSum)
        

    # O(1) time O(1) space
    def sumRange(self, left: int, right: int) -> int:

        totalSum = self.prefixSums[right]
        if left-1 >= 0:
            totalSum -= self.prefixSums[left-1]

        return totalSum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
