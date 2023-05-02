class Solution:
    def minSwaps(self, s: str) -> int:

        # The way to solve this problem:
            # since we are guaranteed an even string that can be balanced once swapped, coutn numbr of open and close brackets
            # if close > open, increment open and decrement close and increment numSwaps
                # thereby, swapping
            # return numSwaps

        # O(n) time O(1) space

        numOpen, numClose = 0, 0
        numSwaps = 0

        for b in s:
            if b == '[':
                numOpen += 1
            elif b == ']':
                numClose += 1
            
            if numClose > numOpen:
                numOpen +=1
                numClose -=1
                numSwaps +=1

        return numSwaps
