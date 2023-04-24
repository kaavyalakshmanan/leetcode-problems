class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # We are given an array of ints where every int appears exactly twice except for one, which appears exactly once
        # We want to return that int that appears exactly once
        # The trivial way to solve this problem would be to use an auxiliary data structure like a hashset
        # But this problem tell su we cannot use extra space
        # The way to solve this is by using bit manipulation
        # Specifically, the xor operation

        # Since everything value except for one appears twice, we know they will cancel each other out and we will be left with the one that apepars exactly once
        # Eg - [4,1,2,1,2]
            # res = 0
            # 0 xor 4 = 4
            # 4 xor 1 = 5
            # 5 xor 2 = 8
            # 8 xor 1 = 6
            # 6 xor 2 = 4
            # dont iterating over the array, answer is 4

        # O(n) time O(1) space

        res = 0
        for num in nums:
            res = res ^ num

        return res
