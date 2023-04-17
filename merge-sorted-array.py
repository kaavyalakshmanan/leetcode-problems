class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # O(n) time O(1) space
        # Pointers
        
        p1, p2, curr = m-1, n-1, (m+n)-1
        while p1 >= 0 or p2 >= 0:
            val1 = nums1[p1] if p1 >= 0 else -inf
            val2 = nums2[p2 ]if p2 >= 0 else -inf

            if val2 > val1:
                nums1[curr] = val2
                p2-=1
            else:
                nums1[curr] = val1
                p1-=1

            curr-=1
