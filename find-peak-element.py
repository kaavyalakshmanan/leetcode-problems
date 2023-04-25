class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # we are given an array of nums and we want to return the index of a peak element
            # a peak element is an element which is greater than left neighbor AND right neighbor
            # we could have multiple peak elements in array, but we just want to return 1
        # the problem tells us we must solve in O(logn) time --> BINARY SEARCH
        # but this is not a sorted array, so once we determine that mid is not a peak element, how do we know which half to continue search on?
        # we know this by looking at which neighbor of mid is larger --> we are guaranteed to find a peak on that half (if both are larger, pick a half)
        # also, if mid happens to be at an edge (0 or len(nums)-1), the problem tells us we can assume it is automatically larger than the left or right side
        # O(logn) time O(1) space

        left, right = 0, len(nums)-1

        while left <= right:
            mid = (right+left)//2

            # left side is greater (where mid > 0 to avoid index out of bounds)
            if mid > 0 and nums[mid] < nums[mid-1]:
                right = mid-1
            # right side is greater
            elif mid < len(nums)-1 and nums[mid] < nums[mid+1]:
                left = mid+1
            # found peak element
            # because either mid is on the edge or its greater than its neighbors
            else:
                return mid

        # dont need a return outside becaude guarnateed a solution

