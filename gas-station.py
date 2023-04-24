class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # Given a gas array where gas[i] tells us how much gas is required at the ith idx, and cost array where cost[i] tells us the cost of gas at that ith idx, where the two arrays are circular, return the starting idx that can make a clockwise loop, else return -1
        # we are guaranteed exactly one solution or 0 solution
        # We can start by figuring out how much it costs at each index (gas[i] - cost[i])
        # gas = [1,2,3,4,5]
        # cost = [3,4,5,1,2]
        # diff = [-2, -2, -2, 3, 3]
        # this tells us that we can either start at the 3rd or 4th index
        # if we start at third index, can we go around a full circle in clockwise position?
            # 3 + 3 - 2 - 2 - 2 = 0
            # which takes us to the 2nd index, so we do a full circle
        # if we start at the fourth idnex, can we go around a full circle in clockwise position?
            # 3 - 2 - 2 = -1
            # we cant even get to the 1st index 
        # the other important thing to note is, sum(gas) >= sum(cost) for a valid circuit since we need enough gas to travel 
            # this could work as a base case
        
        # The way to solve this problem is to use a greedy algo
        # Now that we know the differences, we start at each index with an initial total of 0. we keep adding the current index's value from gas. As soon as we get to < 0, we restart at the next index with a total of 0. If we are able to get to end of array with positive or 0 value, we found the start index

        # O(n) time O(1) space

        if sum(gas) < sum(cost):
            return -1

        total, start = 0, 0
        for i, num in enumerate(gas):
            currCost = gas[i] - cost[i] 
            if total + currCost < 0:
                total = 0
                start = i+1
            else:
                total += currCost

        return start if start < len(gas) else -1

        

        


