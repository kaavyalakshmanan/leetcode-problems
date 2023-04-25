class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # O(n) time O(n) space

        # n = len(nums)//2
        # count = defaultdict(int)

        # for num in nums:
        #     count[num]+=1
        #     if count[num] > n:
        #         return num

        # now lets solve the followup -- how do we do this in O(1) space?
        # lets use the boyer-moore voting algo
        # this is O(n) time O(1) space
        # the way this algo works:
            # keep track of a res and count
            # if currNum == res: increment count
            # else decrement count
            # but whenever count == 0 and currNum != res, we need to reset res to currNum and count back to 1
            # eventually return res 

        count, res = 0, -inf

        for num in nums:
            if num != res and count == 0:
                res = num
                count+=1
            elif num != res:
                count-=1
            else:
                count+=1

        return res


        
