class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        # we are tasked with rearranging input array such that for each element, it does not equal to the average of its neighbors
        # to solve this, we will need to sort the input array because that will make it easier for us to rearrange
        # we also need to realize a math property:
            # for a given number, if its neighbors are strictly less than or strictly greater than it, the average of its neighbors will never equal that number
        # so based off that property, if we sort input array and then rearrange vvalues such that they are alternating (meaning for [1,2,3,4,5] we alternate it to [1,3,2,4,5]) the that property wll be maintained

        # O(nlogn) time O(n) space

        nums.sort()
        res = [0] * len(nums)
        i, j = 0, 0
        while j < len(nums):
            res[i] = nums[j]
            i+=2
            j+=1
            if i >= len(nums):
                i = 1

        

        return res

