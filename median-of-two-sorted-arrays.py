class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # O(log(m+n)) time O(1) space
        
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        total = len(A) + len(B)
        half = total // 2
            
        left, right = 0, len(A)-1 
        
        
        while True:
            midA = (left + right) // 2
            midB = half - midA - 2
            leftA, rightA = A[midA] if midA >= 0 else -inf, A[midA+1] if midA+1 < len(A) else inf
            leftB, rightB = B[midB] if midB >= 0 else -inf, B[midB+1] if midB+1 < len(B) else inf
            
            if leftA <= rightB and leftB <= rightA:
                if (total) % 2 == 1:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB))/2
            elif leftB > rightA:
                left = midA + 1
            else:
                right = midA-1
                
            
