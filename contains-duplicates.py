class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # O(n) time O(n) space
        # Dict

        numsDict = defaultdict(int)
        for num in nums:
            numsDict[num]+=1

        for k, v in numsDict.items():
            if v >= 2:
                return True

        return False
        
