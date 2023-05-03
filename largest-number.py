class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        # O(nlogn) time O(n) space

        for i, num in enumerate(nums):
            nums[i] = str(num)
        
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            return 1

        nums = sorted(nums, key=cmp_to_key(compare))

        s = "".join(nums)

        return str(int(s))
