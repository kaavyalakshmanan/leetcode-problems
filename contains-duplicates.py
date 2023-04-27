class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # O(n) time O(n) space
        # Use a hashmap

        if len(nums) == 1:
            return False

        count = defaultdict(int)

        for num in nums:
            count[num]+=1
            if count[num] == 2:
                return True

        return False
