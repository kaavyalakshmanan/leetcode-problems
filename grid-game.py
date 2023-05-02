class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        # in this problem, we are given a 2D grid where numRows = 2 and numCols = n
        # at each cell you can collect a certain number of points
        # we have 2 robots
        # robot1 goes first and wants to collect as many points as possible from (0, 0) to (1, n-1)
        # every cell that robot1 crosses, the number of points gets set to 0
        # robot2 then goes and tries to collect as many points as possible also from (0,0) to (1, n-1)
        # we want to return the number of points robot2 will collect
        # but the catch is, robot1 goes first, and robot1 will have collected points in a way that minimizes robot2's chance
        # so we need to preemptively know how much its possible for robot2 to collect when robot1 will collect points in a way that destroys 2's chances

        # luckily, all points are positive 
        # the way to solve this problem is using PREFIX SUMS
        # since we only have 2 rows, we will have prefixRow1 and prefixRow2, which will contain all the prefix sums
        # robot1 and robot2 can only move right or down
        # so whichever path robot1 takes, robot2 will have an untaken set of cells to the right and an untaken set of cells to the bottom left

        prefixRow1 = grid[0]
        prefixRow2 = grid[1]
        cols = len(prefixRow1)

        # we've calculated prefix row sums for both rows
        for i in range(1, cols):
            prefixRow1[i] += prefixRow1[i-1]
            prefixRow2[i] += prefixRow2[i-1]

        # res is the result we return
        res = inf

        # now we iterate over cols, and calculate how much is left in right and bottom left if robot1 went down
        # the reason we are only calculating what would happen if robot1 went down is because we already calculated what would happen if robot1 went right, by calculating prefix sums
        for i in range(cols):
            # robot1 goes down at col = i
            # calculate whats left on top right by making use of precomputed prefix sums
            # aka prefixRow[-1] - prefixRow[i] which will give all prefix sums between i and [-1] non inclusive
            topRightLeftover = prefixRow1[-1] - prefixRow1[i]
            # now calculate whats leftover at bottom left, aka everything before i
            bottomLeftLeftover = prefixRow2[i-1] if i-1 >= 0 else 0
            # robot1 will always take a path that minimizes robot2's chances 
            # but robot2 will always try to maximize its own path
            # so thats whats happening here with the max and min
            robot2 = max(topRightLeftover, bottomLeftLeftover)
            res = min(res, robot2)

        return res

        # This is an O(n) time O(n) space solution


        

        

