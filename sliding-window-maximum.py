class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        left = right = 0
        q = collections.deque() # contains indices

        while right < len(nums):
            # remove smaller values in q so q remains monotonically decreasing
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            # if left val of q is no longer in window remove it
            if left > q[0]:
                q.popleft()

            if right+1 >= k:
                res.append(nums[q[0]])
                left+=1

            right+=1

        return res
