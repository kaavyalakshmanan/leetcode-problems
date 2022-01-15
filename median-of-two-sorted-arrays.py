class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # O(log(n)) time O(1) space where n = len(A)
        # Binary Search
        
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
            
        left, right = 0, len(A)-1
        total = len(A) + len(B)
        half = total // 2
        while True:
            midA = (right+left)//2
            midB = half - midA - 2
            
            leftA = A[midA] if midA >= 0 else -inf
            leftB = B[midB] if midB >= 0 else -inf
            rightA = A[midA+1] if midA+1 < len(A) else inf
            rightB = B[midB+1] if midB+1 < len(B) else inf
            
            if leftB <= rightA and leftA <= rightB:
                if total % 2:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
            elif leftA > rightB:
                right = midA-1
            else:
                left = midA + 1
                
            
            
            
        
