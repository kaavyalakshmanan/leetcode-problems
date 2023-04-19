class Solution:
    def mySqrt(self, x: int) -> int:

        # The brute force approach is to iterate from 0 to x and check the squares of each number and return the one that either gives us sqrt(x) or is the closest
        # We would start at 0 because the lowest value that x could be is 0
        # However, this algorithm would be O(sqrt(x)) (since we tehcnically wouldn't go all the way to x, we'd go until we reach swrt(x))
        # We can definitely optimize on this
        # What if we used binary search instead? That would bring time complexity down to O(logn)

        # This algo is O(logn) time O(1) space

        left, right = 0, x

        while left <= right:
            mid = (right+left)//2
            currSquare = mid * mid
            if currSquare == x:
                return mid
            if currSquare > x:
                right = mid-1
            else:
                left = mid+1

        return min(left, right)
