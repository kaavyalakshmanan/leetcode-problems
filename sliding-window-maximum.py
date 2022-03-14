class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # Approach 1: Compute max for every sliding window -- TLE
        # O(n*k) time O(n) space
        
#         start, end = 0, k-1
#         output = []
        
#         while end < len(nums):
#             currMax = max(nums[start:end+1])
#             output.append(currMax)
#             end+=1
#             start+=1
            
            
#         return output
    
        # Approach 2: Monotoniclly Decreasing Q
        
        output = []
        q = collections.deque() # Contains indices
        left, right = 0, 0
        
        while right < len(nums):
            # Pop smaller values from q
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)
            
            # Remove left from q if out of bounds
            if left > q[0]:
                q.popleft()
                
            if (right + 1) >= k:
                output.append(nums[q[0]])
                left+=1
                
            right+=1
            
        return output 
            
            
