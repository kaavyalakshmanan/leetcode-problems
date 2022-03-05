class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # O(n) time O(1) space
        
        k = k % len(nums)
        
        def reverse(arr):
            left, right = 0, len(arr)-1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left+=1
                right-=1
            return arr
        
        # Step 1: reverse array
        reverse(nums)
        mid = k
        
        # Step 2: Reverse first k elements, then reverse remaining
        nums[:mid] = reverse(nums[:mid]) 
        
        # Step 3: Reverse remaining elements
        nums[mid:] = reverse(nums[mid:])
            
        
