class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # O(m+n) time O(1) space
        
        pos = (m+n)-1
        ptr1, ptr2 = m-1, n-1
        
        while pos >= 0:
            val1 = nums1[ptr1] if ptr1 >= 0 else -inf
            val2 = nums2[ptr2] if ptr2 >= 0 else -inf
            
            if val1 > val2:
                nums1[pos] = val1
                ptr1 -= 1
            else:
                nums1[pos] = val2
                ptr2 -= 1
            pos-=1
            
                
