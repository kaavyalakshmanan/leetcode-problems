class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        # O(nlogn) time O(n) space using sorting

        nums.sort()

        left, right = 0, len(nums)-1
        res = 0
        while left < right:
            if nums[left] + nums[right] == k:
                res+=1
                left+=1
                right-=1
            elif nums[left] + nums[right] < k:
                left+=1
            else:
                right-=1

        return res

        # O(n) time O(n) space using hashmap
        numsDict = defaultdict(list)
        res = 0
        for i, n in enumerate(nums):
            if n > k:
                continue
            if numsDict[n]:
                numsDict[n].pop()
                res+=1
            else:
                comp = k-n
                numsDict[comp].append(i)

        return res

            


