class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # n = len(A) m = len(B)
        # O(log(n+m)) time O(1) space
        # Binary search
        
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        left, right = 0, len(A)-1
        total = len(A) + len(B)
        half = total//2
        while True:
            midA = (right+left)//2
            midB = half - (midA+1)-1
            leftA, rightA = A[midA] if midA >= 0 else -inf, A[midA+1] if midA+1 < len(A) else inf
            leftB, rightB = B[midB] if midB >= 0 else -inf, B[midB+1] if midB+1 < len(B) else inf

            if leftA <= rightB and leftB <= rightA:
                if total % 2:
                    return min(rightA, rightB)
                return (min(rightA, rightB) + max(leftA, leftB))/2
            
            if leftB > rightA:
                left = midA+1
            else:
                right = midA-1

        
      

