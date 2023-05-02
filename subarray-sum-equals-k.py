class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # in this problem, we are given an array and we want to return the number of contiguous subarrays that sum to k
        # the brute force approach would be a nested forloop -- O(n^2)
        # could we optimize by using a sliding window approach where once we exceed k, we move the left pointer?
            # no because as per the contraints of the problem, there coul dbe negative values in the array
        # heres how we can reduce brute force solution to a linear solution
        # this algorithm still keeps the basic idea of the brute orce approach, ie lets iterate over array and keep getting the running sum count
        # at each index, we add that value to running sum and we subtract k from that to determine how much we need to remove to get k
        # if that (nums[i] + sumSoFar) - k already exists in the array so far (aka use a dict and check if that prefix sum is in dict), add that key's value to the result
        # otherwise add to dict

        # O(n) time O(n) space

        prefixCount = { 0: 1 }
        total, res = 0, 0

        for num in nums:
            total += num
            if total - k in prefixCount:
                res += prefixCount[total-k]
            if total in prefixCount:
                prefixCount[total]+=1
            else:
                prefixCount[total] = 1

        return res

            
            
