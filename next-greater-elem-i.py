class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # O(n+m) time O(n) space where n = len(nums1) and m = len(nums2)
        # Monotonically decreasing stack

        nums1Dict = {}

        for i, n in enumerate(nums1):
            nums1Dict[n] = i

        res = [-1] * len(nums1)
        stack = []

        for n in nums2:
            while stack and n > stack[-1]:
                prev = stack.pop()
                idx = nums1Dict[prev]
                res[idx] = n
            if n in nums1Dict:
                stack.append(n)

        return res
