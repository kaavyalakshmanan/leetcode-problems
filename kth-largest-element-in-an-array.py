class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # We can get an average time O(n) worst case O(n^2) solution using quickselect
        # How quick select works:
            # In a sorted array, the kth largest element would be nums[len(nums)-k]
            # So we reassign k to that
            # Quick select takes in left and right pointers of the current subarray we care about, and the pivot is always nums[right]
            # We iterate from left to right, if nums[i] <= pivot, we swap nums[i] with pivotIdx (initialized at left), and we increment pivotIdx
            # At the end of the loop, we swap pivotIdx with nums[right]

            # Then we recurse based on the following conditions:
                # If pivotIdx > k, we want to look on the left side, so we recurse by passing in left, pivotIdx-1
                # If pivotIdx < k, we want to look on the right side, so we recurse by passing in pivotIdx+1, right
                # Otherwise, we return nums[k]

        k = len(nums)-k

        def quickSelect(left, right):
            pivot, pivotIdx = nums[right], left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[pivotIdx] = nums[pivotIdx], nums[i]
                    pivotIdx+=1
            nums[pivotIdx], nums[right] = nums[right], nums[pivotIdx]
            if k > pivotIdx:
                return quickSelect(pivotIdx+1, right)
            if pivotIdx > k:
                return quickSelect(left, pivotIdx-1)
            return nums[k]

        return quickSelect(0, len(nums)-1)





