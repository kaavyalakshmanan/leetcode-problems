class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # in this problem, we are given an array and an int k
        # we are tasked with rotating the array so that the ith idx is now
        # in the i+k index

        # we could obviously solve this by using extra space, but can we solve this
        # in O(1) space?
        # yes, by reversing the array, then reversing the first k elements, and the remaining n-k elements

        # step 1: mod k by length of input
        # we do this because k could be larger than the array input and we would go out of bounds
        # this way if k == len(nums), we are rotating array 0 times
        k = k % len(nums)

        # step 2: reverse input array
        self.reverseArray(nums, 0, len(nums)-1)

        # step 3: reverse the first k elements
        self.reverseArray(nums, 0, k-1)

        # step 4: reverse the remaining elements
        self.reverseArray(nums, k, len(nums)-1)

        # O(n) time O(1) space

    def reverseArray(self, nums: List[int], l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1

        
