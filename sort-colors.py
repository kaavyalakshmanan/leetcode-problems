class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # O(n) time O(1) space
        # Using bucket sort
        # Make two passes oer input array

        count = [0] * 3
        for num in nums:
            count[num]+=1

        numIdx = 0

        for i, c in enumerate(count):
            for j in range(c):
                nums[numIdx] = i
                numIdx+=1

        # Slightly more efficient solution where we just make 1 pass over input array
        # This algorithm is QuickSort and involves partitioning the array where
        # everything to left of left pointer is 0, everything to right of right pointer is 2
        # we have a curr pointer which is the curr idx in nums we are looking at
        # If curr idx is pointing at a 2, swap with right and decrement right
        # If curr idx is pointing at 0, swap with left and increment left
        # Keep doing this until curr reaches right
        # But when do we increment curr?
        # curr should be incremented when curr swaps with left, because we want to make sure that curr is ONLY incrementing when it has swapped with left, to make sure that ALL lefts are to the left of left
        # This avoids tricky edge cases where curr prematurely increments but theres a 0 to the right of left that will forever remain there 
        # And if we maintain the property of everything to LEFT of left WILL ALWAYS BE 0, everything to RIGHT of right WILL ALWAYS BE 2, this will never happen

        # This is O(n) time O(1) space but only 1 pass over nums

        left, right, curr = 0, len(nums)-1, 0

        # We do <= not < because whatever right is pointing to hasnt been processed yet
        while curr <= right:
            if nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right-=1
            elif nums[curr] == 0:
                nums[curr], nums[left] = nums[left], nums[curr]
                left+=1
                curr+=1
            # If nums[curr] == 1, basically a no-op
            else:
                curr+=1
                




