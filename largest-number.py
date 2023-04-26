class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        # we are given an array of ints
        # we want to rearrange the ints such that they form the largest int
        # we want to return that as a string

        # step 1: since the output needs to be a string, convert each input into a string
        for i, n in enumerate(nums):
            nums[i] = str(n)

        # step 2: define a helper fn which will be used to compare 2 strings and return the larger one
        def compare(s1, s2):
            # we can do string comparators like this in python
            # we're concatenating s1 and s2 and comparing based on that
            if s1 + s2 > s2 + s1:
                return -1
            return 1

        # step 3: use python's library functio sorted(), and paas in compare to sort the input array nums
        # cmp_to_key is a python thing
        nums = sorted(nums, key=cmp_to_key(compare))

        # step 4: now that nums has been sorted, lets use pythons join() function to join all the strings in nums into one string
        s = "".join(nums)

        # step 5: deal with the corner case of input array is [0, 0, 0] --> this would return "000"
        # we actually want that to return "0"
        # so lets convert s into an int to get rid of leading 0s
        i = int(s)

        # step 6: but we actually want to return a string, so lets convert i back into a string and return it
        return str(i)

        # O(nlogn) time O(n) space


