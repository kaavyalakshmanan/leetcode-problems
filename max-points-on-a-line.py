class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        # in this problem, we are given a points array consisting of (x,y) coordinates on a plane
        # the task is to return the max number of points that lie on the same line

        # the brute force approach:
            # for every pair of points, what are all the points that lie on that line?
                # this is an n^3 algo
        # instead, here is an optimized approach

        # for each point, determine if it lies on the longest line
        # count all points with the same slope
        # update result with max

        # O(n^2) time O(n) space

        res = 1

        for i in range(len(points)-1):
            slope = 0
            p1 = points[i]
            count = defaultdict(int)
            for j in range(i+1, len(points)):
                p2 = points[j]
                # The formula for calculating slope is (y2-y1)/(x2-x1)
                # if x1 == x2, we would get a division by 0 error
                # to avoid this, handle this as edge case and set slope to infinity
                if p1[0] == p2[0]:
                    slope = float("inf")
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                count[slope]+=1
                res = max(res, count[slope]+1)

        return res

