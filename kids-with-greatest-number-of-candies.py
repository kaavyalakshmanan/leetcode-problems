class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        # O(n) time O(n) space

        maxNum = max(candies)
        res = [False] * len(candies)

        for i, num in enumerate(candies):
            if num + extraCandies >= maxNum:
                res[i] = True

        return res
