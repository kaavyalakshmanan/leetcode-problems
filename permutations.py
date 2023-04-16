class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # O(n!) time O(n!) space
        # n! because we are getting all possible permutations of something and number of possible permutations of [1,2,3] is 3 * 2 * 1 = 6 hence n!
        # We are recursing so thats why its n! space

        res = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            currNum = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(currNum)

            res.extend(perms)
            nums.append(currNum)

        return res
