class Solution:
    def minFlips(self, s: str) -> int:

        # given an input string consisting of binary characters, where we are allowed to either move s[0] to s[-1] or flip a 0 into 1 / 1 into 0, what is the min number of flips we can make to make entire string alternating?
        # aka, maximize number of mvoes form 0 to -1 to minimize number of flips
        # given a string of length n, we have 2 possibilities for what the string of same length can end up as: either beginning with 0 or 1 and just alternating
        # if we construct those possibilities of size 2n each, and also expand input string to size 2n, its akin to moving each n element to end of string
        # then we can compare the difference between the 2 possibility strings and take the min]
        # O(n) time O(n) space

        s1, s2 = "", ""
        for i in range(len(s)*2):
            s1+= "0" if i % 2 else "1"
            s2+= "1" if i % 2 else "0"

        s3 = s + s
        print(s1, s2, s3)
        res = 0
        diff1, diff2 = 0, 0
        left, right = 0, 0

        while right < len(s):
            if s3[right] != s1[right]:
                diff1 += 1
            if s3[right] != s2[right]:
                diff2 += 1
            right+=1

        currDiff1, currDiff2 = diff1, diff2


        while right < len(s3):
            
            if s3[left] != s1[left]:
                currDiff1-=1
            if s3[right] != s1[right]:
                currDiff1+=1
            
            if s3[left] != s2[left]:
                currDiff2-=1
            if s3[right] != s2[right]:
                currDiff2+=1

            diff1 = min(diff1, currDiff1)
            diff2 = min(diff2, currDiff2)

            left+=1
            right+=1

        return min(diff1, diff2)




